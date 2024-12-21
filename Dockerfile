# Use a lightweight Python image
FROM python:3.11-slim

# Install wkhtmltopdf and system dependencies
RUN apt-get update && apt-get install -y wkhtmltopdf xfonts-75dpi

# Set the working directory inside the container
WORKDIR /app

# Copy your Flask app to the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 10000 (Render default)
EXPOSE 10000

# Command to run Flask app
CMD ["python", "app.py"]
