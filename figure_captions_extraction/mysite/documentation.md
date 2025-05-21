
# 🧬 Figure Captions Extraction System 

## Overview

The **Figure Captions Extraction System** is a Django-based web application designed to extract figure captions and related metadata from scientific articles using PMC (PubMed Central) or PMID (PubMed Identifier) identifiers. The system offers both a user-friendly web dashboard and a RESTful API, facilitating data retrieval in JSON and CSV formats. It integrates with PubTator for biomedical entity recognition and provides comprehensive logging for monitoring and debugging.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Web Dashboard](#web-dashboard)
  - [API Usage](#api-usage)
- [Modules Description](#modules-description)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Features

- **Web Dashboard**: Interactive interface to submit PMC/PMID identifiers and view extracted data.
- **REST API**: Programmatic access to extraction functionalities.
- **Data Formats**: Supports JSON and CSV outputs.
- **Entity Extraction**: Integrates with PubTator for biomedical entity recognition.
- **Logging**: Comprehensive logging for monitoring and debugging.
- **Docker Support**: Containerized deployment using Docker and Docker Compose.

---

## Project Structure

figure_captions_extraction/
├── .venv/ # Virtual environment
├── myenv/ # Alternative virtual environment
├── mysite/ # Django project directory
│ ├── admin_screenshots/ # Screenshots for documentation
│ ├── extractor/ # Core application
│ │ ├── api/ # API views and URLs
│ │ ├── ingestion/ # Data ingestion modules
│ │ ├── management/ # Custom management commands
│ │ ├── migrations/ # Database migrations
│ │ ├── templates/ # HTML templates
│ │ ├── logs/ # Log files
│ │ ├── admin.py # Admin configurations
│ │ ├── api.py # API logic
│ │ ├── db_storage.py # Database storage utilities
│ │ ├── models.py # Database models
│ │ ├── pmc_fetcher.py # PMC data fetching logic
│ │ ├── pubtator.py # PubTator integration
│ │ ├── test.py # Test scripts
│ │ ├── tests.py # Unit tests
│ │ ├── urls.py # URL configurations
│ │ └── views_dashboard.py # Dashboard views
│ ├── mysite/ # Django settings and WSGI/ASGI
│ │ ├── init.py
│ │ ├── asgi.py
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── wsgi.py
│ ├── db.sqlite3 # SQLite database
│ ├── extractor_figure.csv # Sample CSV output
│ ├── extractor_paper.csv # Sample CSV output
│ ├── manage.py # Django management script
├── .env # Environment variables
├── .env.bak # Backup of environment variables
├── .gitignore # Git ignore file
├── docker-compose.yml # Docker Compose configuration
├── Dockerfile # Dockerfile for containerization
├── documentation.md # Detailed documentation
├── h.txt # Miscellaneous notes
├── requirements.txt # Python dependencies
└── tests_ids.txt # Test PMC/PMID IDs

yaml
Copy
Edit

---

## Installation

### Prerequisites

- Python 3.8+
- pip
- Virtual environment tool (`venv` or `virtualenv`)
- Docker and Docker Compose (optional, for containerized deployment)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/figure_captions_extraction.git
   cd figure_captions_extraction
Create and Activate Virtual Environment

bash
Copy
Edit
python3 -m venv myenv
source myenv/bin/activate
Install Dependencies

bash
Copy
Edit
pip install --upgrade pip
pip install -r requirements.txt
Apply Migrations

bash
Copy
Edit
python manage.py migrate
Run the Development Server

bash
Copy
Edit
python manage.py runserver
Access the Application

Web Dashboard: http://127.0.0.1:8000/dashboard/

API Endpoint: http://127.0.0.1:8000/api/extract/

Usage
Web Dashboard
Accessible at http://127.0.0.1:8000/dashboard/, the dashboard allows users to:

Submit PMC or PMID identifiers.

View extracted figure captions and metadata.

Download results in JSON or CSV formats.

API Usage
Endpoint
POST /api/extract/

Request Body
json
Copy
Edit
{
  "ids": ["PMC1234567", "PMID7654321"],
  "format": "json"
}
ids: List of PMC or PMID identifiers.

format: Desired output format (json or csv).

Response
JSON Format

json
Copy
Edit
{
  "results": [
    {
      "id": "PMC1234567",
      "title": "Sample Title",
      "abstract": "Sample Abstract",
      "figures": [
        {
          "caption": "Figure 1 caption.",
          "entities": ["Entity1", "Entity2"]
        }
      ]
    }
  ]
}
CSV Format

Returns a CSV file with columns: ID, Title, Abstract, Figure Caption, Entities.

Modules Description
pmc_fetcher.py: Fetches and parses XML data from PMC.

pubtator.py: Integrates with PubTator for entity extraction.

views_dashboard.py: Handles dashboard views and submissions.

api/views.py: Manages API endpoints and responses.

ingestion/: Contains modules for data ingestion and processing.

db_storage.py: Utilities for database interactions.

models.py: Defines database models.

admin.py: Configures Django admin interface.

Testing
To run tests:

bash
Copy
Edit
python manage.py test
Ensure that the tests_ids.txt file contains valid PMC/PMID identifiers for testing purposes.

Deployment
Environment Variables
Create a .env file in the root directory with the following variables:

env
Copy
Edit
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=127.0.0.1,localhost
Docker Setup (Optional)
To run the application using Docker:

Build the Docker Image

bash
Copy
Edit
docker build -t figure_captions_extraction .
Run the Docker Container

bash
Copy
Edit
docker-compose up
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch: git checkout -b feature/your-feature-name

Make your changes and commit them: git commit -m 'Add some feature'

Push to the branch: git push origin feature/your-feature-name

Submit a pull request.

Please ensure your code adheres to the project's coding standards and passes all tests.

License
This project is licensed under the MIT License.

Acknowledgements
Django

PubTator
"""

yaml
Copy
Edit

---

**Now you can copy all of this Python code in one shot**, and it contains the entire README content exactly as markdown text, including all fenced code blocks inside it, preserving the formatting perfectly.

If you want me to help with anything else or save this as a file, just ask
