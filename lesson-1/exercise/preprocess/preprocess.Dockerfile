FROM python:3.12-slim

WORKDIR /app

COPY preprocess/requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY preprocess/src src

# WORKDIR src

CMD ["python", "src/preprocess.py"]