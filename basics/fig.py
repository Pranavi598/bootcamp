import requests
import xml.etree.ElementTree as ET
from typing import Optional, List


def fetch_pmc_xml(pmc_id: str) -> str:
    url = f"https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/{pmc_id}/unicode"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch paper: {pmc_id}")
    return response.text


def get_text_by_infon(document: ET.Element, key: str, value: str) -> Optional[str]:
    """Helper to get text content by infon key-value."""
    for passage in document.findall("passage"):
        for infon in passage.findall("infon"):
            if infon.attrib.get("key") == key and infon.text and infon.text.lower() == value:
                text_elem = passage.find("text")
                if text_elem is not None and text_elem.text:
                    return text_elem.text.strip()
    return None


def extract_figures(document: ET.Element) -> List[str]:
    """Extract all figure captions from document."""
    figures = []
    for passage in document.findall("passage"):
        for infon in passage.findall("infon"):
            if infon.attrib.get("key") == "section_type" and infon.text and infon.text.lower() == "fig":
                text_elem = passage.find("text")
                if text_elem is not None and text_elem.text:
                    figures.append(text_elem.text.strip())
                    break
    return figures


def parse_figure_captions(xml_str: str) -> dict:
    root = ET.fromstring(xml_str)
    document = root.find("document")
    if document is None:
        raise ValueError("No document found in XML")

    title = get_text_by_infon(document, "section_type", "title") or get_text_by_infon(document, "type", "title")
    abstract = get_text_by_infon(document, "type", "abstract")
    figures = extract_figures(document)

    return {
        "title": title or "",
        "abstract": abstract or "",
        "figures": figures
    }


if __name__ == "__main__":
    pmc_id = "PMC6821181"
    xml_content = fetch_pmc_xml(pmc_id)
    paper_data = parse_figure_captions(xml_content)
    print(paper_data)
