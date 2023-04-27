FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip
COPY requirements/production.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /opt

WORKDIR /opt

COPY ./docker/backend/start /start
RUN chmod +x /start

