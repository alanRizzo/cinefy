FROM python:3.11-alpine

RUN apk update && apk upgrade && apk add --no-cache gcc=12.2.1_git20220924-r10 libc-dev=0.7.2-r5 libffi-dev=3.4.4-r2

# https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE
# Prevents Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1

# ensures that the python output is sent straight to terminal (e.g. your container log)
# without being first buffered and that you can see the output of your application (e.g. django logs)
# in real time. Equivalent to python -u: https://docs.python.org/3/using/cmdline.html#cmdoption-u
ENV PYTHONUNBUFFERED 1

ENV PORT=8011

# FIXIT: just to connect to the dokcer database image
ENV DB_HOST="localdb"

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

# execute project
CMD ["python", "-m", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "src.main:app"]
