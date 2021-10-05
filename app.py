import json
import os

from flask import Flask, make_response, jsonify
from flask.logging import logging

app = Flask(__name__)

app.logger.setLevel(logging.INFO)


class NoHealth(logging.Filter):
    def filter(self, record):
        return 'GET /health' not in record.getMessage()


logging.getLogger("werkzeug").addFilter(NoHealth())


@app.route("/")
def hi():
    path_to_time_obj = os.getenv("PATH_TO_TIME_DATA")
    with open(path_to_time_obj) as fp:
        data = json.load(fp)
        return make_response(jsonify(data), 200)


@app.route("/health")
def health():
    return make_response(jsonify({"ok": True}), 200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
