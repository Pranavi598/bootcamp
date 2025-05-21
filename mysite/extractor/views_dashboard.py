from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .pmc_fetcher import fetch_pmc_xml, parse_figure_captions
import csv
import json

# Temporary storage for extraction results
EXTRACTION_RESULTS = []


def dashboard_view(request):
    return render(request, 'dashboard.html', {
        'results': EXTRACTION_RESULTS
    })


def submit_ids(request):
    global EXTRACTION_RESULTS
    if request.method == 'POST':
        raw_input = request.POST.get('paper_ids', '')
        ids = [pid.strip() for pid in raw_input.replace(',', '\n').split('\n') if pid.strip()]
        EXTRACTION_RESULTS.clear()

        for pmc_id in ids:
            try:
                xml_data = fetch_pmc_xml(pmc_id)
                parsed = parse_figure_captions(xml_data)
                for fig in parsed['figures']:
                    EXTRACTION_RESULTS.append({
                        'paper_id': pmc_id,
                        'title': parsed['title'],
                        'abstract': parsed['abstract'],
                        'caption': fig['caption'],
                        'entities': fig.get('entities', [])
                    })
            except Exception as e:
                EXTRACTION_RESULTS.append({
                    'paper_id': pmc_id,
                    'title': '',
                    'abstract': '',
                    'caption': f'Error: {str(e)}',
                    'entities': []
                })
        return redirect('dashboard')
    else:
        return redirect('dashboard')


def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="results.csv"'

    writer = csv.writer(response)
    writer.writerow(['Paper ID', 'Title', 'Abstract', 'Caption', 'Entities'])

    for item in EXTRACTION_RESULTS:
        writer.writerow([
            item['paper_id'],
            item['title'],
            item['abstract'],
            item['caption'],
            ', '.join(e.get('name', str(e)) for e in item['entities'])
        ])
    return response


def download_json(request):
    return JsonResponse(EXTRACTION_RESULTS, safe=False)
