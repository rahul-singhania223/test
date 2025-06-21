FROM python:3.12-slim

WORKDIR /app

COPY main.py main.py
COPY requirements.txt requirements.txt
COPY app.py app.py

RUN pip install -r requirements.txt

CMD [ "python", "app.py"]