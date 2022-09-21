FROM python:3.9.12-slim

RUN apt-get update

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# env variable to detect if python runs from container
ENV PYTHONBUFFERED 1
