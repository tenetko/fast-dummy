FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT 1

WORKDIR /usr/src/app

COPY ./* ./
COPY --from=frontend_builder app/frontend/build ./static

RUN pip install --upgrade pip \
&& pip install poetry \
&& poetry install --no-root\

EXPOSE 80
CMD ["sh", "-c", "~/.venv/bin/uvicorn main:app --host=0.0.0.0 --port=$PORT"]
