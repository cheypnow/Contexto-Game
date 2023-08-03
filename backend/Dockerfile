FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y \
    curl \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /

CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]