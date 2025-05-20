# 📘 Project Documentation: Figure Caption Extraction and Access System

---

## 🎯 Purpose

This project is a Django-based system that extracts, stores, and exposes figure captions and metadata from scientific papers (currently from **PubMed Central**). It also identifies biological entities like gene names using the **PubTator API**.

---

## ✅ System Overview

### Key Features

- Accepts a list of PMCIDs via CLI
- Extracts:
  - Title
  - Abstract
  - Figure Captions
  - Figure URLs
  - Biological Entities (from captions)
- Stores data in a **SQLite** database
- Exposes data through a REST API (JSON format)
- Dockerized for deployment
- Logging and configuration managed via `.env`

---

## 📁 Project Structure

```
figure_captions_extraction-Copy/
├── .env                  # Environment variables (API keys, settings)
├── Dockerfile            # Docker config
├── docker-compose.yml    # Optional Docker Compose
├── README.md             # Usage guide
├── documentation.md      # Project documentation (you’re reading this!)
├── db.sqlite3            # Default database
├── extractor_figure.csv  # Exported data
├── extractor_paper.csv   # Exported data
├── manage.py             # Django CLI entry
├── requirements.txt      # Python dependencies
├── tests_id.txt          # Input PMCIDs
├── admin_screenshots/    # Django admin screenshots (optional)
├── mysite/               # Django settings and WSGI
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── extractor/            # Main app
    ├── api.py
    ├── db_storage.py
    ├── models.py
    ├── pmc_fetcher.py
    ├── pubtator.py
    ├── admin.py
    ├── management/
    │   └── commands/
    │       └── ingest_paper.py   # Batch ingestion CLI
    ├── watcher/
    │   ├── file_ingester.py
    │   ├── watcher.py
    │   └── upload-ingester.py
    └── api/                      # Optional: DRF views

## 🧱 Architecture

### Components

| Component                  | Description                                                  |
|----------------------------|--------------------------------------------------------------|
| `ingestion/`               | Handles fetching and parsing of PMC articles                 |
| `pmc_fetcher.py`           | Fetches XML using BioC API, parses figure captions           |
| `pubtator.py`              | Fetches biological entities from PubTator                    |
| `db_storage.py`            | Saves extracted data into database using Django ORM          |
| `management/commands/ingest.py` | Custom Django command for batch ingestion from file       |
| `api/`                     | (Optional) REST endpoints using DRF (if enabled)             |
| `models.py`                | Defines `Paper`, `Figure`, and `Entity` models               |
| `.env`                     | Stores secrets and configuration                             |
| `Dockerfile`               | Docker setup                                                  |
| `README.md`                | Usage instructions                                           |

---

## 📦 Technologies Used

- Python 3.x
- Django
- SQLite
- Requests
- PubTator API
- BioC PMC API
- Docker
- dotenv

---

## 🛠️ CLI Usage

### Ingesting Data

```bash
python manage.py ingest --input pmc_ids.txt
```

### Sample CLI Output

```
Ingesting 3 IDs from pmc_ids.txt…
✅ Success: 2
❌ Errors: 1
PMC1234567: Failed to parse figure data
```

---

## 🔐 Authentication & Config

### .env Configuration

```
DEBUG=True
API_KEY=your_api_key_here
LOG_LEVEL=INFO
DATABASE_URL=sqlite:///db.sqlite3
```

### Logging Setup (`settings.py` or a logging config file)

```python
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'root': {
        'handlers': ['console'],
        'level': os.getenv("LOG_LEVEL", "INFO"),
    },
}
```

---

## ⚙️ Deployment (Docker)

### Build & Run

```bash
docker build -t figure-extractor .
docker run -p 8000:8000 --env-file .env figure-extractor
```

---

## 🧪 Sample API (if enabled)

```bash
GET /api/figures/?paper_id=PMC1234567
```

Response (JSON):

```json
[
  {
    "paper_id": "PMC1234567",
    "figure_number": "Fig 1",
    "caption": "Expression of BRCA1 and BRCA2 genes...",
    "url": "https://.../fig1.jpg",
    "entities": ["BRCA1", "BRCA2"]
  }
]
```

---

## 📋 Error Handling & Logging

- All exceptions are logged using logging module
- Batch CLI ingestion prints per-ID errors
- Successful ingestions are confirmed with a count

---

## 🚦 Status Summary After Your Work

✅ What has been done:

- ✅ CLI batch ingestion using `--input` flag
- ✅ Support for JSON responses
- ✅ `.env` config for data source and logging level
- ✅ Used PMC as data source
- ✅ Captions, metadata, and entity extraction
- ✅ Logging with INFO/DEBUG levels
- ✅ Dockerized for deployment
- ✅ Success/failure logs and exit status

---

## 📈 Future Improvements

- Add support for **PMID** (currently only PMC)
- Expand data sources beyond PMC
- Add CSV download via API
- Add HTML frontend or Swagger UI for REST docs

---
