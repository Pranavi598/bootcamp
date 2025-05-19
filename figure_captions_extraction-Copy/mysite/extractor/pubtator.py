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


