from flask import Flask, jsonify, request

from backends import get_backends

app = Flask(__name__)
app.config.from_object("config")


@app.route("/redispatch/", methods=["POST"])
def redispatch():
    data = request.get_data()
    if not data:
        return jsonify({"error": "No data recieved"})
    res = {}
    for backend in get_backends(app):
        error = None
        try:
            backend.redispatch(data)
        except Exception as e:
            # Could use a better exception handling and logging system
            error = str(e)
        res[backend.get_target_name()] = "success" if not error else error
    if res:
        return jsonify(res)
    return jsonify({"error": "No backends were ready"})
