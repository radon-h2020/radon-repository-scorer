FROM python:3.8-buster

MAINTAINER Stefano Dalla Palma

RUN python3.8 -m pip install --upgrade pip

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python3.8", "main.py"]