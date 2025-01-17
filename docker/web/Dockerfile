FROM python:3.11-slim

WORKDIR /project

# Copy project files
COPY pyproject.toml .
COPY poetry.lock .

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean

# Install Poetry
RUN pip install --no-cache-dir poetry

RUN poetry install

COPY . .
