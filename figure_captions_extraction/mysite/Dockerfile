# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run Django commands on start (optional)
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]
