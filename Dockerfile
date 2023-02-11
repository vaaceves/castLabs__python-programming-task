FROM python:3.8.16-bullseye

COPY proxy/requirements.txt .

RUN mkdir /app
RUN pip install -r requirements.txt

WORKDIR /app

EXPOSE 8000