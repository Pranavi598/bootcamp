
# 📚 Figure Captions Extraction

This project is a Django-based web application that extracts figure captions and related metadata (such as title, abstract, entities) from scientific articles using **PMC** and **PubTator** APIs. The system is being developed as part of a bootcamp with a focus on production-readiness, modular architecture, and real-time monitoring.

---

## 🔧 Project Structure (So Far)

```
figure_captions_extraction/
│
├── mysite/
│   ├── api/                  # Django API views for frontend/backend integration
│   ├── ingestion/           # Scripts for pulling figure and metadata from PMC & PubTator
│   ├── management/
│   │   └── commands/
│   │       └── ingest.py     # Custom Django management command to ingest data
│   ├── templates/            # HTML templates for frontend
│    
│   ├── models.py             # Django models for storing extracted data
│   ├── tasks.py              # Background processing and helper functions
│   └── ...
│
├── Dockerfile                # Dockerfile for running Django app
├── docker-compose.yml        # Docker Compose for managing services
├── requirements.txt          # Python dependencies
└── README.md                 # You are here
```

---

## ✅ Features Implemented

- [x] Django project setup and modular app (`extractor`)
- [x] Integrated PMC & PubTator APIs
- [x] Custom ingestion command: `python manage.py ingest "<PMC_ID>"`
- [x] Data stored in Django models: articles, figures, captions, and entity mentions
- [x] Basic frontend using templates to display extracted metadata
- [x] Dockerfile for containerizing the Django app
- [x] `docker-compose.yml` setup (pending Docker daemon setup)
- [x] Running and testing inside WSL (Ubuntu 22.04)
- [x] FastAPI considered for future monitoring layer (in progress)

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

## 🛠️ Features

- [ ] Add real-time monitoring using FastAPI
- [ ] Expose ingestion progress via API
- [ ] Add logging and error handling
- [ ] Add tests and CI pipeline
- [ ] Polish Docker Compose setup after fixing Docker daemon issues




# Simple Web Server Setup

This project demonstrates a simple web server running on an Azure Virtual Machine. It displays my name and photo using a basic HTML file, and includes command-line demonstrations recorded via Asciinema.

## Setup Instructions

### 1. Created `index.html`
A basic HTML file was created with the following content:

```html
<html>
  <body>
    <h1>Your Name: Pranavi</h1>
    <img src="photo11.jpg" alt="photo11">
  </body>
</html>
```

### 2. Transferred Photo
The image file `photo11.jpg` was transferred to the remote Azure VM using the VS Code Explorer drag-and-drop functionality. This allowed copying files from the local machine to the remote server without using SCP or CLI-based methods.

### 3. Started Web Server
A simple HTTP server was started using Python with the following command inside the terminal of the Azure VM:

```bash
python3 -m http.server 80
```

### 4. Accessed via Public IP
The web page was accessed by entering the public IP of the Azure Virtual Machine in a browser:  
`http://4.247.27.166/bootcamp/`

### 5. Command-Line Application Demonstration
You can see a recording of the command-line actions, including navigating directories and starting the web server, in the following Asciinema recordings:

- Web Server Setup Recording: [Web Server Setup Recording](https://asciinema.org/a/K86gAnbSbuzspRdvkT1GBe2jP)
- Docker Demo Recording: [Docker Demo Recording](https://asciinema.org/a/pdvVf1HCSKUdZvECk74NTL8WM)

### 6. Folder Structure

```
bootcamp/
  └── DAY 0/
      ├── index.html
      ├── photo11.jpg
      ├── webserver.cast
      ├── docker.cast
      ├── README.md
      └── .gitignore
```

