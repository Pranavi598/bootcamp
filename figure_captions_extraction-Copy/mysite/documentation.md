# Developer Hand-off Brief: Figure Caption Extraction and Access System

## 🎯 Purpose

We are building a Django-based system that extracts figure captions and associated metadata from scientific publications (specifically from PubMed Central). The system supports:

* Extracting title, abstract, figure captions, and figure URLs
* Identifying key biological entities (e.g., genes) in captions using PubTator API
* Storing extracted data in a SQLite database
* Querying and retrieving data via a REST API

This is a beginner-friendly implementation developed by a fresher with hands-on experience in Django and Python.

## ✅ High-Level User Expectations

### 👤 As a User

* I can submit a list of PMC or PMID IDs.
* I can retrieve extracted figure data via an API.
* I can get responses in JSON or CSV formats.
* I can upload lists of paper IDs via the API.

### 🛠️ As an Admin

* I can configure:

  * Location of SQLite DB
  * API access credentials (simple key-based auth)
  * Logging level (INFO or DEBUG)
  * Data source (PMC for now)


### ⚙️ As an Ops Person

* I can run ingestion via Django custom commands
* I can deploy using Docker
* I get clean startup and shutdown messages

---

## 📝 What I Expect From You

### 1. Design Document

#### 🧱 Architecture Overview

* **Backend**: Django app named `extractor`
* **Database**: SQLite (default `db.sqlite3`)
* **APIs**: Built using Django views and DRF (if added later)
* **External APIs**:

  * BioC API (for paper structure)
  * PubTator API (for named entity recognition)

#### 🔑 Key Components

* `ingestion/`: Scripts to fetch and parse paper metadata
* `api/`: Exposes REST endpoints for data access
* `models.py`: Defines database schema
* `management/commands/ingest.py`: Django CLI for ingestion
* `views.py`: Renders web views (if enabled)
* `templates/`: (Optional, if HTML frontend is added)

#### 🧩 Dependencies

* `requests`: for HTTP requests to PMC and PubTator APIs
* `Django`: web framework
* `sqlite3`: built-in DB for local use
* `python-dotenv`: for config management

### 2. Implementation and Testing Plan

#### 🔄 Phased Development

1. **Setup Django project** and `extractor` app
2. **Define models**: Paper, Figure, Entity
3. **Wrote ingestion script** using BioC and PubTator APIs
4. **Expose data via API endpoints**
5. **Test on real PMC IDs** and edge cases
6. **Add Docker support**


#### ✅ Testing Plan

* Unit tests for ingestion pipeline (mocked data)
* Manual testing with real PMC IDs
* API testing via curl/Postman
* Validating DB records via Django Admin

### 3. Implementation

Directory structure:

```
figure_captions_extraction/
├── extractor/
│   ├── api/
│   ├── ingestion/
│   ├── management/commands/ingest.py
│   ├── models.py
│   ├── templates/
│   ├── views.py
├── db.sqlite3
├── Dockerfile
├── requirements.txt
├── README.md
```

#### Features Implemented

* Ingests data for a given list of PMC IDs
* Extracts title, abstract, captions, figure URLs
* Gets biological entities from PubTator
* Stores all in SQLite using Django ORM
* Exposes a basic REST API (or JSON web views)
* Uses `.env` file for config (API key, log level)
* CLI command: `python manage.py ingest --file pmc_ids.txt`

### 4. Operationalization

#### 📘 README Highlights

* How to run server: `python manage.py runserver`
* How to ingest: `python manage.py ingest --file your_file.txt`
* Where data is stored: `db.sqlite3`
* Docker support: `docker build -t figure-extractor . && docker run -p 8000:8000 figure-extractor`
* Access API: `http://localhost:8000/api/figures/`

#### 🧪 Sample Usage

```
# Run ingestion
python manage.py ingest --file sample_ids.txt

# Start server
python manage.py runserver

# Visit API
http://127.0.0.1:8000/api/figures/?paper_id=PMC1234567
```

---

## figure-caption-extraction system

* Clean, working system based on Django and SQLite
* Design choices ( SQLite for simplicity, Django for built-in admin and ORM)
* Realistic handling of errors, missing captions, and empty API responses
* README and Dockerfile included

---

Let me know if you want me to auto-generate a `README.md`, `requirements.txt`, or Dockerfile based on this.
