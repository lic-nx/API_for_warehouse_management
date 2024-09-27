# Pull base image
FROM python:3.9

# Get environment varibles
ARG DEBUG

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /src

# Install dependencies

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /src

EXPOSE 8000