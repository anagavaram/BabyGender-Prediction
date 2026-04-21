FROM python:3.13-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libgomp1 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY data/ ./data/
COPY models/ ./models/
COPY notebooks/ ./notebooks/

CMD ["python", "src/main.py"]
