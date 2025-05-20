from django.conf import settings
from django.http import JsonResponse
from functools import wraps
from django.views.decorators.csrf import csrf_exempt
import json

from extractor.models import Paper
from extractor.pmc_fetcher import fetch_pmc_xml, parse_figure_captions
from extractor.db_storage import save_paper_to_db


def api_key_required(view_func):
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        api_key = request.headers.get('X-API-KEY') or request.GET.get('api_key')
        if api_key != settings.API_KEY:
            return JsonResponse({'error': 'Forbidden: invalid API key'}, status=403)
        return view_func(request, *args, **kwargs)
    return _wrapped

@csrf_exempt
@api_key_required
def submit_ids(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method allowed'}, status=405)
    try:
        body = json.loads(request.body)
        ids = body.get('pmc_ids')
        if not ids or not isinstance(ids, list):
            return JsonResponse({'error': 'pmc_ids must be a list'}, status=400)

        results = []
        for pmc_id in ids:
            try:
                xml = fetch_pmc_xml(pmc_id)
                data = parse_figure_captions(xml)
                save_paper_to_db(pmc_id, data)
                results.append({'pmc_id': pmc_id, 'status': 'success'})
            except Exception as e:
                results.append({'pmc_id': pmc_id, 'status': 'error', 'message': str(e)})
        return JsonResponse({'results': results})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_key_required
def get_paper_data(request):
    pmc_id = request.GET.get("pmc_id")
    if not pmc_id:
        return JsonResponse({"error": "pmc_id parameter is required"}, status=400)

    # Try DB first, otherwise ingest on the fly
    try:
        paper = Paper.objects.get(pmc_id=pmc_id)
    except Paper.DoesNotExist:
        try:
            xml = fetch_pmc_xml(pmc_id)
            data = parse_figure_captions(xml)
            save_paper_to_db(pmc_id, data)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
        paper = Paper.objects.get(pmc_id=pmc_id)

    response = {
        "pmc_id": paper.pmc_id,
        "title": paper.title,
        "abstract": paper.abstract,
        "figures": [
            {
                "caption": fig.caption,
                "entities": [e.entity for e in fig.entities.all()]
            }
            for fig in paper.figures.all()
        ]
    }
    return JsonResponse(response)

def health(request):
    return JsonResponse({'status': 'ok'})
