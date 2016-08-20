FROM python:3.5-alpine
ENV PYTHONUNBUFFERED 1
ENV REDIS_HOST "redis"
RUN mkdir /code
RUN mkdir /db
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt
RUN python manage.py migrate
