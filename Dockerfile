# Use official lightweight Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8501

# Set working directory
WORKDIR /app

# Install system dependencies (build-essential, curl, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Make startup script executable and convert Windows line endings to Unix line endings
RUN chmod +x start.sh && sed -i -e 's/\r$//' start.sh

# Expose the Streamlit and FastAPI ports
EXPOSE 8501
EXPOSE 8000

# Run the startup script
ENTRYPOINT ["/bin/bash", "./start.sh"]
