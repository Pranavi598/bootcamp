#
#
# from .models import Paper, Figure, Entity
#
# def save_paper_to_db(pmc_id: str, paper_data: dict):
#     paper, _ = Paper.objects.get_or_create(
#         pmc_id=pmc_id,
#         defaults={"title": paper_data["title"], "abstract": paper_data["abstract"]}
#     )
#
#     # Avoid duplicating figures if paper already exists
#     if not paper.figures.exists():
#         for fig in paper_data["figures"]:
#             figure = Figure.objects.create(paper=paper, caption=fig["caption"])
#             for entity in fig.get("entities", []):
#                 Entity.objects.create(figure=figure, entity=str(entity))
from .models import Paper, Figure, Entity
import logging

logger = logging.getLogger(__name__)

def save_paper_to_db(pmc_id: str, paper_data: dict):
    logger.info(f"Saving paper with PMC ID: {pmc_id}")

    paper, created = Paper.objects.get_or_create(
        pmc_id=pmc_id,
        defaults={"title": paper_data["title"], "abstract": paper_data["abstract"]}
    )

    if created:
        logger.info(f"Created new Paper entry for PMC ID: {pmc_id}")
    else:
        logger.info(f"Paper with PMC ID {pmc_id} already exists")

    if not paper.figures.exists():
        logger.info(f"Adding figures for paper {pmc_id}")
        for fig in paper_data["figures"]:
            figure = Figure.objects.create(paper=paper, caption=fig["caption"])
            logger.debug(f"Created Figure: {fig['caption']}")
            for entity in fig.get("entities", []):
                Entity.objects.create(figure=figure, entity=str(entity))
                logger.debug(f"Created Entity: {entity}")
    else:
        logger.info(f"Figures already exist for paper {pmc_id}, skipping figure creation.")
