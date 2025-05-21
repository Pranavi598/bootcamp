# 🧾 Project Documentation: Figure Captions Extraction

**Author**: Pranavi  
**Project**: Bootcamp – Figure Caption & Metadata Extraction using Django  
**Last Updated**: May 19, 2025  

---

## 📘 Overview

This Django project is designed to extract and store **figure captions**, **titles**, **abstracts**, and **biomedical entities** from scientific research articles using the **PMC Open Access** API and **PubTator Central**.

The core goals of this system are:
- To build a production-ready ingestion pipeline
- To modularize API consumption, parsing, and database storage
- To expose a user-friendly web interface (and later, monitoring APIs)
- To containerize the system with Docker

---

## 🧱 Project Architecture

```
figure_captions_extraction/
│
├── mysite/                        # Django project folder
│   ├── api/                       # (Planned) REST endpoints for ingestion and status
│   ├── ingestion/                 # Core logic for pulling PMC and PubTator data
│   ├── management/
│   │   └── commands/
│   │       └── ingest.py          # Custom CLI command to trigger ingestion
│   ├── templates/                 # HTML pages showing extracted data
│   ├── 
│   ├──                 
│   ├── models.py                  # Django ORM models
│   └── ...
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker setup (in progress)
├── docker-compose.yml             # Multi-service configuration
└── README.md                      # Project overview
```

---

## ⚙️ Key Components

### 1. `models.py`

Defines Django models for storing:
- **Article** – Metadata like title, abstract, PMC ID
- **Figure** – Caption and figure link
- **Entity** – Extracted biomedical terms (gene, disease, etc.)

These models are linked using foreign keys for relational querying.

---

### 2. `ingestion/` – PMC & PubTator Logic

This folder contains Python functions to:
- Fetch full text and figures from the **PMC Open Access API**
- Fetch named entities from **PubTator Central**
- Clean, parse, and prepare for storage

---

### 3. `management/commands/ingest.py`

Custom management command to ingest a single article:

```bash
python manage.py ingest PMC1234567
```

This command:
- Accepts a valid **PMC ID**
- Fetches and parses both PMC + PubTator data
- Calls model layer to persist to the database
- Logs output and errors

---

### 4. `views.py` and `templates/`

Currently minimal, but supports rendering:
- Extracted titles
- Abstracts
- Figure captions
- Entities

This part will grow to include visualizationI.

---



## 🧪 How to Use

### Method 1: Without Docker (WSL/Virtualenv)

```bash
# Activate virtual environment
source myenv/bin/activate

# Navigate to Django folder
cd mysite

# Run migrations
python manage.py migrate

# Ingest a sample article
python manage.py ingest PMC1234567

# Start server
python manage.py runserver
```

### Method 2: Docker (Planned)

```bash
# Once Docker daemon is fixed
docker-compose build
docker-compose up
```

This will bring up:
- Django app container
- PostgreSQL or SQLite (optional volume)
- Future: FastAPI monitor service

---

## 🔍 Ingestion Pipeline: How It Works

1. **User Input**: `python manage.py ingest PMCxxxxxxx`
2. **PMC API Fetch**: Title, abstract, and figure XML data
3. **PubTator Fetch**: Biomedical named entities
4. **Parse + Store**: Save into Django models
5. **View Output**: Render in HTML or query via admin

---

## 📊 Example PMC Article

For `PMC1234567`:

- Title: _"Effect of XYZ on ABC"_
- Abstract: _"This study explores..."_
- Figures:
  - **Figure 1**: "Schematic of the treatment model"
  - **Figure 2**: "Results after 10 days"
- Entities: [Gene: TP53], [Chemical: Doxorubicin], [Disease: Cancer]

---

## 🪛 Developer Notes

- **WSL (Ubuntu 22.04)** is being used for development
- Django version: 4.x
- Python version: 3.10+
- 
- Docker Compose integration is partially complete 

---

## 🗺️ Roadmap

Features:                             

| PMC + PubTator ingestion         
| Ingestion management command        
| Basic HTML template rendering       
| Dockerfile                        
| Docker Compose                      
| FastAPI monitoring dashboard        
| Ingestion progress & error logging 



