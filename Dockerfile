FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_PATH /usr/src/app/

WORKDIR /usr/src/app

COPY . ./

RUN pip install --upgrade pip \
&& pip install poetry \
&& poetry install --no-root

EXPOSE 80
CMD poetry run python -m uvicorn main:app --host=0.0.0.0 --port=$PORT
