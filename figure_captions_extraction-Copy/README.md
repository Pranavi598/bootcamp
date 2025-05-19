# 📚 Figure Captions Extraction

This project is a Django-based web application that extracts figure captions and related metadata (such as title, abstract, entities) from scientific articles using **PMC** and **PubTator** APIs. The system is being developed as part of a bootcamp with a focus on production-readiness, modular architecture, and real-time monitoring.

---

## 🔧 Project Structure (So Far)

```
```
figure_captions_extraction-Copy/mysite
├── .env
├── .env.bak
├── .venv/
├── Dockerfile
├── README.md
├── admin_screenshots/
├── db.sqlite3
├── docker-compose.yml
├── documentation.md
├── extractor_figure.csv
├── extractor_paper.csv
├── manage.py
├── mysite/
│   ├── mysite/
│   ├── scripts/
│   └── __init__.py
        ingest_from_file
├── mysite/
│   ├── __init__.py
│   ├── asgi.py
│   ├── db.sqlite3
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── seed_list.txt
└── extractor/
    ├── __init__.py
    ├── admin.py
    ├── api.py
    ├── db_storage.py
    ├── models.py
    ├── pmc_fetcher.py
    ├── pubtator.py
    ├── test.py
    ├── tests.py
    ├── api/
    └── management/
        └── commands/
```

```

---

## ✅ Features Implemented

- [x] Django project setup and modular app (`extractor`)
- [x] Integrated PMC & PubTator APIs
- [x] Custom ingestion command: `python manage.py ingest "<PMC_ID>"`
- [x] Data stored in Django models: articles, figures, captions, and entity mentions
- [x] Dockerfile for containerizing the Django app
- [x] `docker-compose.yml` setup (pending Docker daemon setup)
- [x] Running and testing inside WSL (Ubuntu 22.04)

---

## 🐳 Docker Setup 

### Requirements
- Docker Desktop running on Windows
- WSL integration enabled (`Ubuntu-22.04`)
- Docker daemon must be active before running these commands

### Steps to Build and Run :

```bash
# Build the containers
docker-compose build

# Run the containers
docker-compose up
```

---

## 🧪 Local Development (WSL / Virtualenv)

You can also run the project manually without Docker:

```bash
# Activate virtual environment
source myenv/bin/activate

# Navigate to the Django project
cd mysite

# Run migrations
python manage.py migrate

# Run the ingestion command (example PMC ID)
python manage.py ingest PMC1234567

# Start development server
python manage.py runserver
```

---

## 🔍 Example Output (From Ingestion)

After running:

```bash
python manage.py ingest PMC1234567
```

The system:
- Fetches metadata (title, abstract, figure captions)
- Parses PubTator annotations (gene, disease, chemical entities)
- Stores everything in the database
- Renders on a simple HTML page (WIP)

---





