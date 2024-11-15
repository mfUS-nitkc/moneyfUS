FROM python:3.13.0-bullseye AS stg

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

FROM stg AS dev

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--settings=config.settings.develop"]

FROM python:3.13.0-slim-bullseye AS build

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY --from=stg /app .

ENV PYTHONUSERBASE=/app/__pypackages__
RUN pip install --user -r requirements.txt

FROM gcr.io/distroless/python3-debian12

WORKDIR /app
COPY --from=build /app .

EXPOSE 8000

ENV PYTHONUSERBASE=/app/__pypackages__
ENTRYPOINT ["sh", "-c", "python manage.py runserver 0:8000 --settings=config.settings.deploy"]

