FROM python:3.12-slim

WORKDIR /app

COPY ingest/requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ingest/src src

WORKDIR src

CMD ["python", "ingest.py"]