from flask import Flask, make_response, jsonify
from flask.logging import logging
from flask.scaffold import F
app = Flask(__name__)
import yaml

app.logger.setLevel(logging.INFO)


class NoHealth(logging.Filter):
    def filter(self, record):
        return 'GET /health' not in record.getMessage()


logging.getLogger("werkzeug").addFilter(NoHealth())


@app.route('/config')
def config_test():
    with open("example.yaml", "r") as stream:
        try:
            print(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)
            return make_response(jsonify({"ok": False}), 200)

    return make_response(jsonify({"ok": True}), 200)


@app.route("/")
def hello_world():
    # @ todo fucking catch exceptions
    # foo ={}
    # try:
    #     return foo.get('asshir')
    # except Exception:
    #     print("fuck")

    #     return "asdfs"
    return "<p>Hello, World!</p>"


@app.route("/health")
def health():
    return make_response(jsonify({"ok": True}), 200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
