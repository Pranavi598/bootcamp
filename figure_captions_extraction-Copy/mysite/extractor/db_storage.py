from .models import Paper, Figure, Entity

def save_paper_to_db(pmc_id: str, paper_data: dict):
    paper, _ = Paper.objects.get_or_create(
        pmc_id=pmc_id,
        defaults={"title": paper_data["title"], "abstract": paper_data["abstract"]}
    )

    # Avoid duplicating figures if paper already exists
    if not paper.figures.exists():
        for fig in paper_data["figures"]:
            figure = Figure.objects.create(paper=paper, caption=fig["caption"])
            for entity in fig.get("entities", []):
                Entity.objects.create(figure=figure, entity=str(entity))
