FROM debian:12-slim AS stg

ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel

FROM stg AS dev

COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

COPY . /app

ENTRYPOINT [ "/app/docker-entrypoint.sh", "--settings=config.settings.develop" ]

FROM stg AS build-venv

COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

FROM busybox:1.37.0-glibc AS busybox

FROM gcr.io/distroless/python3-debian12:nonroot AS deploy

WORKDIR /app

COPY --from=busybox /bin/sh /bin/sh

COPY --from=build-venv /venv /venv
COPY . /app

EXPOSE 8000

ENV PYTHONUNBUFFERED 1
ENTRYPOINT [ "/bin/sh", "/app/docker-entrypoint.sh", "--settings=config.settings.deploy" ]
