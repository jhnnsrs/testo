FROM python:3.8-slim-buster


RUN pip install "arkitekt[cli]==0.4.29"


RUN mkdir /app
COPY . /app
WORKDIR /app