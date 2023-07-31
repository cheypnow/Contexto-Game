FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY docker /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]