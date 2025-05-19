# extractor/pubtator.py
import requests
from typing import List, Dict


def extract_entities_from_text(text: str) -> List[Dict]:
    url = "https://www.ncbi.nlm.nih.gov/research/pubtator-api/annotations/annotate/"
    params = {
        "text": text,
        "concepts": "gene,disease,chemical,species,mutation"
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(url, data=params, headers=headers)

    if response.status_code == 404:
        return []  # No entities found, but not an error
    elif response.status_code != 200:
        raise ValueError(f"Failed to extract entities: {response.status_code}")

    result = response.json()

    entities = []
    for ann in result.get("denotations", []):
        entities.append({
            "id": ann.get("id"),
            "type": ann.get("obj"),
            "start": ann.get("span", {}).get("begin"),
            "end": ann.get("span", {}).get("end"),
            "text": text[ann.get("span", {}).get("begin"):ann.get("span", {}).get("end")]
        })

    return entities
#import requests
#from typing import List, Dict

# def extract_entities_from_pmid(pmid: str) -> List[Dict]:
#     url = f"https://www.ncbi.nlm.nih.gov/research/pubtator-api/annotations/pmids/{pmid}"
#     headers = {
#         "Accept": "application/json"
#     }
#
#     response = requests.get(url, headers=headers)
#
#     if response.status_code == 404:
#         return []  # No entities found
#     elif response.status_code != 200:
#         raise ValueError(f"Failed to extract entities: {response.status_code} -> {response.text}")
#
#     data = response.json()
#
#     entities = []
#     for passage in data.get("passages", []):
#         for ann in passage.get("annotations", []):
#             start = ann.get("locations", [{}])[0].get("offset")
#             length = ann.get("locations", [{}])[0].get("length")
#             text = passage.get("text", "")[start : start + length]
#             entities.append({
#                 "id": ann.get("id"),
#                 "type": ann.get("infons", {}).get("type"),
#                 "start": start,
#                 "length": length,
#                 "text": text
#             })
#
#     return entities


