FROM python:3.9-slim-buster

ENV BIND_PORT 5000
ENV REDIS_HOST localhost
ENV REDIS_PORT 6379

COPY . /app
WORKDIR /app
RUN ls
RUN python3 -m pip install -r ./requirements.txt

EXPOSE $BIND_PORT
CMD python3 run.py