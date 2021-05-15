FROM python:3.9-buster
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY gisapp ./gisapp
COPY proto ./proto

ENTRYPOINT ["poetry", "run", "python", "-m", "gisapp"]
