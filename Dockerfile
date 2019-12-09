FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . . 

ENV FLASK_APP = app.py 

CMD flask run --host=0.0.0.0

