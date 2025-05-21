# 🧬 Figure Caption Extraction System

A Django-based system to **extract**, **store**, and **serve** figure captions and biomedical entities from scientific publications using PMC and PubTator APIs.

---

## 🌟 Features

- 🔍 Fetch metadata, captions, and images from **PMC**
- 🧠 Extract **biomedical entities** via **PubTator**
- 🗃️ Store results in **SQLite** using Django ORM
- 🔁 Supports **batch ingestion**
- 🛠️ REST API endpoints (optional)
- ⚙️ Environment-driven with `.env`
- 🐳 Docker support
- 📂 File-watcher to auto-process uploaded input files

---

## 📂 Directory Structure (Simplified)

```
figure_captions_extraction-Copy/
├── .env
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── README.md
├── documentation.md
├── requirements.txt
├── tests_id.txt
├── extractor/
│   ├── models.py
│   ├── admin.py
│   ├── api.py
│   ├── db_storage.py
│   ├── pmc_fetcher.py
│   ├── pubtator.py
│   ├── watcher/
│   │   ├── watcher.py
│   │   ├── file_ingester.py
│   │   └── upload-ingester.py
│   └── management/
│       └── commands/
│           └── ingest_paper.py
└── mysite/
    ├── settings.py
    ├── urls.py
    └── ...
```

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Setup `.env`

```ini
DEBUG=True
LOG_LEVEL=INFO
API_KEY=your_pubtator_api_key
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Ingest PMCIDs (Batch)

```bash
python manage.py ingest_paper --input tests_id.txt
```

---

## 🔁 File Watcher Mode

To auto-process new files (in watcher mode):

```bash
python extractor/watcher/watcher.py
```

Or to upload and ingest:

```bash
python extractor/watcher/upload-ingester.py --file path/to/your_file.txt
```

---

## 🔌 Sample API (if integrated)

**GET /api/figures/?paper_id=PMC1234567**

```json
[
  {
    "paper_id": "PMC1234567",
    "figure_number": "Fig. 2",
    "caption": "TP53 expression...",
    "url": "https://...",
    "entities": ["TP53"]
  }
]
```

---

## 🧾 Logging

Your `.env` defines log level:

```ini
LOG_LEVEL=INFO
```

Output (in terminal):

```
2025-05-19 12:00:00 [INFO] extractor.pmc_fetcher: Downloaded PMC1234567
2025-05-19 12:00:00 [DEBUG] extractor.pubtator: Entities: ['TP53']
```

---

## 🐳 Docker Usage

### Build

```bash
docker build -t figure-caption-extractor .
```

### Run

```bash
docker run --env-file .env -p 8000:8000 figure-caption-extractor
```

---

## 📸 Django Admin

Navigate to `/admin/` to manage `Paper`, `Figure`, and `Entity` entries.

---

## 📌 Future Ideas

- Add Swagger UI
- PostgreSQL support
- Frontend integration (React/Vue)
- Scheduling or cron-based ingestion

---

## 🧠 Author

Built with ❤️ by **Pranavi** during a data engineering bootcamp.

