# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.12

FROM python:${PYTHON_VERSION}-slim AS python-base

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=${PORT:-9095} \
    PIP_CACHE_DIR=/.cache

# Update the base OS
RUN --mount=type=cache,target="/var/cache/apt",sharing=locked \
    --mount=type=cache,target="/var/lib/apt/lists",sharing=locked \
    set -eux; \
    apt-get update; \
    apt-get upgrade -y; \
    apt install --no-install-recommends -y  \
        git; \
    apt-get autoremove -y

COPY requirements.txt .
RUN --mount=type=cache,target=${PIP_CACHE_DIR},sharing=locked \
    pip install -r requirements.txt

COPY . .

EXPOSE 9095

CMD gunicorn --preload --bind :$PORT --workers 1 --threads 8 --timeout 0 _wsgi:app
