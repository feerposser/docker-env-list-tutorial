FROM python:3

LABEL MAINTAINER = "Fernando Posser Pinheiro | feerposser"

WORKDIR /app

COPY app.py /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

CMD python app.py