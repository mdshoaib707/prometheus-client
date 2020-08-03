FROM python:3.7.8-alpine

RUN mkdir -p /app

WORKDIR /app/

ADD . /app/

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]
