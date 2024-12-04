FROM python:3.12-slim

WORKDIR /app

COPY model/requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY model/src src

# WORKDIR src

CMD ["python", "src/model.py"]