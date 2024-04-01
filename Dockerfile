FROM python:3.11-alpine

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt

COPY ./ ./