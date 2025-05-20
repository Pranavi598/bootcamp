import requests
import xml.etree.ElementTree as ET


def fetch_pmc_xml(pmc_id: str) -> str:
    url = f"https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/{PMC_ID}/unicode"
    resp = requests.get(url)
    if resp.status_code != 200:
        raise ValueError(f"Failed to fetch paper: {pmc_id}")
    return resp.text


def parse_figure_captions(xml_str: str):
    root = ET.fromstring(xml_str)

    title = ""
    abstract = ""
    figures = []

    # Get the first document only (main paper)
    document = root.find("document")
    if document is None:
        raise ValueError("No document found in XML")

    # Extract title
    for passage in document.findall("passage"):
        for infon in passage.findall("infon"):
            if infon.attrib.get("key") == "section_type" and infon.text.lower() == "title":
                text_elem = passage.find("text")
                if text_elem is not None and text_elem.text:
                    title = text_elem.text.strip()
                    break
        if title:
            break

    # If title not found, fallback to 'title' type
    if not title:
        for passage in document.findall("passage"):
            for infon in passage.findall("infon"):
                if infon.attrib.get("key") == "type" and infon.text.lower() == "title":
                    text_elem = passage.find("text")
                    if text_elem is not None and text_elem.text:
                        title = text_elem.text.strip()
                        break
            if title:
                break

    # Extract abstract
    for passage in document.findall("passage"):
        for infon in passage.findall("infon"):
            if infon.attrib.get("key") == "type" and infon.text.lower() == "abstract":
                text_elem = passage.find("text")
                if text_elem is not None and text_elem.text:
                    abstract = text_elem.text.strip()
                    break
        if abstract:
            break

    # Extract figure captions
    for passage in document.findall("passage"):
        type_val = ""
        for infon in passage.findall("infon"):
            if infon.attrib.get("key") == "section_type" and infon.text.lower() == "fig":
                text_elem = passage.find("text")
                if text_elem is not None and text_elem.text:
                    figures.append(text_elem.text.strip())
                    break

    return {
        "title": title,
        "abstract": abstract,
        "figures": figures
    }


if __name__ == "__main__":
    xml = fetch_pmc_xml("PMC6821181")
    data = parse_figure_captions(xml)
    print(data)

