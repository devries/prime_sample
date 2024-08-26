FROM registry.hub.docker.com/library/python:3.9-slim
ENV POETRY_VERSION=1.7.1

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app
COPY . .
RUN poetry install
CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0:8080", "app:app"]
