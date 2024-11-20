FROM python:3.11.0-bullseye AS stg

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

FROM stg AS dev

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--settings=config.settings.develop"]

FROM python:3.11.0-bullseye AS build

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY --from=stg /app .

RUN pip install -r requirements.txt

FROM gcr.io/distroless/python3-debian12 AS deploy

WORKDIR /app

COPY --from=build /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=build /usr/local/bin /usr/local/bin
COPY --from=build /app .

ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages
EXPOSE 8000

ENV PYTHONUNBUFFERED 1
CMD ["manage.py", "runserver", "0.0.0.0:8000", "--settings=config.settings.deploy"]

