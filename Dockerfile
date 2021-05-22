FROM python:3.9
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8080
CMD ./gunicorn.sh
