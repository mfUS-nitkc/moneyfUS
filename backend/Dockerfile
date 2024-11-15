FROM python:3.13.0-bullseye AS stg

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

FROM stg AS dev

CMD ["echo", "/app/.env"]

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--settings=config.settings.develop"]
