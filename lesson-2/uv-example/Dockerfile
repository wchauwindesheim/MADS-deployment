# Base image
FROM python:3.12

WORKDIR /app

ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

COPY ./requirements.txt .
RUN /root/.local/bin/uv pip install --system --no-cache -r requirements.txt

COPY test.py test.py
ENTRYPOINT ["python", "test.py"]


