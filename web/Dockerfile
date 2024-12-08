FROM python:3.9-slim

WORKDIR /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

CMD ["python", "app.py"]
