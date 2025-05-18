FROM python:3.13

WORKDIR /app

COPY pyproject.toml poetry.lock* ./
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

COPY . .

EXPOSE 8000

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]