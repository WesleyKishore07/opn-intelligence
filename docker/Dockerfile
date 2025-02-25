FROM python:3.10-slim

WORKDIR /app

ARG DEPLOY_ENV
ARG PASSPHRASE
ENV DEPLOY_ENV=$DEPLOY_ENV
ENV PASSPHRASE=$PASSPHRASE


USER root

ENV PYTHONPATH="/app:$PYTHONPATH"
     
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    pkg-config \
    libmariadb-dev \
    libmariadb-dev-compat && \
    rm -rf /var/lib/apt/lists/*

COPY requirements/ /app/requirements/

RUN pip install --no-cache-dir -r requirements/requirements.txt
RUN apt-get update && apt-get install -y bash

COPY env /app/env
COPY . /app


RUN chmod +x /app/decrypt.sh

RUN /app/decrypt.sh > /dev/null 2>&1


EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]