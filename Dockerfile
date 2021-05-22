FROM python:3.9-slim-buster
COPY . /app
WORKDIR /app
EXPOSE 8080
RUN pip3 install -r requirements.txt
CMD gunicorn run:app -w 1 --threads 4 -b 0.0.0.0:8080
