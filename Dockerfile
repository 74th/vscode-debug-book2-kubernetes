FROM python:3.9-buster
WORKDIR /app
RUN pip install poetry && poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY gisapp ./gisapp
COPY proto ./proto

ENTRYPOINT ["python", "-m", "gisapp"]
