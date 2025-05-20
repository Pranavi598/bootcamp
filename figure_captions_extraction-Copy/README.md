# 🧠 Figure Captions Extraction System

This project extracts figure captions and metadata (titles, abstracts, entities, etc.) from scientific research articles using the PMC and PubTator APIs. It supports both CLI and REST API-based ingestion, provides authentication, and logs progress with detailed statuses.

---

## 📁 Project Structure

```
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
```

---

## ✅ Features

* Extract figure captions from PMC Open Access articles
* Use PubTator API for biomedical entity tagging
* CLI ingestion using `manage.py ingest`
* REST API ingestion (`POST /api/submit_ids/`)
* API key authentication
* Logs results (success, error, syntax issues)
* JSON output format
* Modular for future extension (e.g., arXiv, bioRxiv)

---

## 🚀 Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Create `.env` file

```ini
# .env
X_API_KEY=ABCDEF67890
```

---

### 3. Start Django server

```bash
python manage.py runserver
```

---

## 💪 CLI Ingestion Example

```bash
python manage.py ingest --input data/pmc_ids.txt
```

Expected output:

```
PMC8674544 - Success
PMC9536536 - Failed: syntax error
```

---

## 🌐 API Ingestion Example

```bash
curl -X POST http://127.0.0.1:8000/api/submit_ids/ \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: ABCDEF67890" \
  -d '{"pmc_ids": ["PMC1852221", "PMC6821181"]}'
```

Returns JSON like:

```json
[
  {"pmc_id": "PMC1852221", "status": "error", "message": "syntax error"},
  {"pmc_id": "PMC6821181", "status": "success"}
]
```

---

## 🔒 API Authentication

All POST requests must include a valid header:

```
X-API-KEY: ABCDEF67890
```

The key is stored securely in your `.env` file.

---

## 📜 Logging

Logging is defined in `logging_config.py`:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
```

To change verbosity, modify `level=logging.INFO` to `DEBUG`, `WARNING`, etc.

---

## 🔤 Input File Format

Example `pmc_ids.txt`:

```
PMC8674544
PMC9536536
```

---

## 🌍 Data Source

Currently supported:

* ✅ PMC Open Access Subset (XML)
* ✅ PubTator (entity recognition)

Designed to support future extensions (e.g., arXiv, bioRxiv).

---

## 🛠️ Future Enhancements

* Add PDF caption extraction
* Add monitoring dashboard
* Add background job queue (Celery)
* Store results in PostgreSQL or S3

---


