FROM ubuntu:jammy

RUN apt-get update && apt-get install -y \
	tesseract-ocr \
	libtesseract-dev \
	python3-pip \
	poppler-utils

WORKDIR /app

COPY . .

RUN mkdir -p /app/results

RUN pip install -r requirements.txt
