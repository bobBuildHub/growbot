FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy application code
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Ensure gunicorn is installed
RUN pip install gunicorn

# Expose application port
EXPOSE 5000

# Command to start the application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "web.app:app"]
