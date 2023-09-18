FROM python:3.11-alpine

RUN apk update && apk upgrade && apk add --no-cache gcc=12.2.1_git20220924-r10 libc-dev=0.7.2-r5 libffi-dev=3.4.4-r2

ENV PORT=8011

WORKDIR /home/app/cinefy

# install poetry
RUN pip install poetry
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1
ENV PATH="$PATH:$POETRY_HOME/bin"

# copy project files
COPY cinefy/poetry.lock .
COPY cinefy/pyproject.toml .

# install dependencies
RUN poetry install --no-cache --only main

COPY cinefy/alembic.ini .
COPY cinefy/create_db.py .
COPY cinefy/migrations/. migrations/.
COPY cinefy/src/. src/.

# switch to non root user
USER $USERNAME

# EXPOSE 80

# execute project
CMD ["python", "-m", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "src.main:app"]
