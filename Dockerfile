FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* ./
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

COPY . .

EXPOSE 8000

RUN python src/manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "src.core.wsgi:application"]
