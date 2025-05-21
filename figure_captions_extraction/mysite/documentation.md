# 📘 Documentation: Figure Captions Extraction System

## 🔍 Objective

This project is a full-stack Django-based application that extracts **figure captions and metadata** from biomedical research articles using **PMC IDs** or **PMID IDs**. It integrates with the **PubTator API** to fetch biomedical named entities for each caption. The system provides both a **web dashboard** and a **REST API** for interaction.

---

## 🚀 Key Functionalities

- 🖼️ Extract figure captions and metadata from PMC articles.
- 🔬 Recognize biomedical entities (e.g., genes, proteins, diseases) using PubTator.
- 🌐 Provide a web dashboard for interactive data visualization and extraction.
- 📡 Offer a REST API for programmatic access to extraction features.
- 📁 Output available in JSON or CSV formats.
- 🛠️ Modular, testable code with clear separation of concerns.
- 🐳 Docker support for consistent deployment across environments.
- 📜 Logging and error-handling for better monitoring and debugging.

---

## 🏗️ Project Layout (Structure + Explanation)

```
figure_captions_extraction/
├── mysite/                     # Main Django project
│   ├── extractor/              # Django app containing core logic
│   │   ├── api/                # API views, serializers, endpoints
│   │   ├── ingestion/          # Data fetching/parsing logic
│   │   ├── management/         # Custom CLI commands (e.g., ingest)
│   │   ├── templates/          # HTML templates for the dashboard
│   │   ├── admin.py            # Admin interface configuration
│   │   ├── api.py              # Unified API logic for caption/entity extraction
│   │   ├── db_storage.py       # Save data into Django models
│   │   ├── models.py           # ORM definitions for Article, Figure, Entity
│   │   ├── pmc_fetcher.py      # Functions to fetch and parse PMC XML
│   │   ├── pubtator.py         # Interface to PubTator API
│   │   ├── tests.py            # Unit and integration test cases
│   │   ├── urls.py             # App-level routing for views and API
│   │   └── views_dashboard.py  # Web dashboard views
│   ├── settings.py             # Django project settings
│   ├── urls.py                 # Root URL dispatcher
│   └── wsgi.py / asgi.py       # WSGI/ASGI app entry points
├── db.sqlite3                  # Local development database
├── extractor_figure.csv        # Output: figure-level data
├── extractor_paper.csv         # Output: article-level metadata
├── manage.py                   # Django management CLI
├── requirements.txt            # Python dependency list
├── docker-compose.yml          # Docker Compose services definition
├── Dockerfile                  # Docker image setup
├── .env                        # Local environment variables
├── tests_ids.txt               # Sample test input IDs (PMC/PMID)
```

---

## 🧠 How It Works (Step-by-Step)

1. **User Input**  
   - A list of PMC or PMID IDs is submitted via the dashboard or API.

2. **PMC Article Fetching**  
   - For PMC IDs, `pmc_fetcher.py` fetches XML full text from NCBI’s servers.
   - Extracts:
     - Article title
     - Abstract
     - Each `<fig>` tag and its caption content.

3. **Entity Recognition via PubTator**  
   - Each caption is sent to the PubTator API (`pubtator.py`).
   - Returns biomedical annotations like:
     - Genes
     - Proteins
     - Chemicals
     - Diseases, etc.

4. **Database Storage**  
   - `db_storage.py` writes the processed data into Django models:
     - `Article` → contains multiple `Figure` entries
     - `Figure` → contains multiple recognized `Entity` records

5. **Result Presentation**  
   - Web dashboard displays data interactively.
   - REST API allows result download in JSON or CSV formats.

---

## ✅ Example Input/Output

### 🔽 Input

- **Web Form Input**:  
  `PMC1234567`

- **API POST Body**:

```json
{
  "ids": ["PMC1234567", "PMID7654321"],
  "format": "json"
}
```

---

### 📤 Output (JSON)

```json
{
  "results": [
    {
      "id": "PMC1234567",
      "title": "Advances in Neural Imaging",
      "abstract": "This study explores...",
      "figures": [
        {
          "caption": "Figure 2. MRI scan showing neural activity...",
          "entities": ["neural activity", "MRI", "brain"]
        }
      ]
    }
  ]
}
```

---

### 📥 Output (CSV)

| ID         | Title                   | Figure Caption                         | Entities                |
|------------|-------------------------|----------------------------------------|--------------------------|
| PMC1234567 | Advances in Neural...   | Figure 2. MRI scan showing neural...   | neural activity, MRI     |

---

## 🌐 Dashboard

Visit: `http://localhost:8000/dashboard/`

- 🔎 Paste multiple IDs separated by space or comma.
- 📊 View parsed results and download in JSON/CSV.
- ⚠️ Shows status if any ID fails to fetch or parse.

---

## 🧰 API Reference

### Endpoint

```
POST /api/extract/
```

### Request Body

```json
{
  "ids": ["PMC1234567", "PMID7654321"],
  "format": "csv"
}
```

- `ids`: Required. List of PMC/PMID identifiers.
- `format`: Optional. `json` (default) or `csv`.

### Response

- `200 OK`: Returns extracted data.
- `400 Bad Request`: Malformed input or unsupported ID.

---

## ⚙️ Setup Instructions

### 🔧 Local Development

```bash
# Clone the repo
git clone https://github.com/yourname/figure_captions_extraction.git
cd figure_captions_extraction

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up database
python manage.py migrate

# Run local server
python manage.py runserver
```

Then go to: `http://127.0.0.1:8000/dashboard/`

---

## 🐳 Docker Deployment

### Option 1: Dockerfile

```bash
docker build -t fig-extractor .
docker run -p 8000:8000 fig-extractor
```

### Option 2: Docker Compose

```bash
docker-compose up --build
```

Accessible at `http://localhost:8000/`

---

## 🧪 Testing

### Run Django Tests

```bash
python manage.py test
```

Test cases use IDs listed in `tests_ids.txt`.

---

## 🧠 Technologies Used

- **Python** & **Django** – Backend and ORM.
- **Django REST Framework** – API support.
- **Django** – UI design.
- **PubTator API** – Entity recognition.
- **NCBI E-utilities** – Article metadata.
- **Docker / Docker Compose** – Containerization.
- **SQLite / PostgreSQL** – Database.

---

## 🔮 Future Improvements

- Support more formats: DOI, arXiv.
- Add visual rendering of figures (not just captions).
- Implement caching with Redis for PubTator results.
- Use Celery for async bulk ingestion.
- Enable user login to save history.
- Switch to PostgreSQL + Redis in production.

---

## 🙌 Credits

- PubTator Central by NCBI
- PubMed Central Open Access Subset
- Django  
