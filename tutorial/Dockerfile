FROM python:3

LABEL MAINTAINER = "Fernando Posser Pinheiro | feerposser"

WORKDIR /app

COPY app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD python app.py