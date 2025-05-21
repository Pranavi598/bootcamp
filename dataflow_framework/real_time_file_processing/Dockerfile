# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install any needed packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Run the file watcher by default
CMD ["python3", "main.py", "--watch"]
