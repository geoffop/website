import os

from flask import Flask, render_template, send_from_directory
from flask_manage_webpack import FlaskManageWebpack
from gevent import monkey
from gevent.pywsgi import WSGIServer
from redis import Redis

app = Flask("app")
redis = Redis(host=os.environ["REDIS_HOST"], port=os.environ["REDIS_PORT"])
bind_port = int(os.environ["BIND_PORT"])
manage_webpack = FlaskManageWebpack()
manage_webpack.init_app(app)
#https://pypi.org/project/Flask-Manage-Webpack/

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hits")
def hello():
    redis.incr("hits")
    total_hits = redis.get("hits").decode()
    return f"Hello from Redis! I have been seen {total_hits} times."


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


if __name__ == "__main__":
    monkey.patch_all()
    http_server = WSGIServer(("0.0.0.0", bind_port), app)
    http_server.serve_forever()
