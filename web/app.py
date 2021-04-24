"""
John Doe's Flask API.
"""

import config
import os
from flask import Flask, render_template, abort, send_from_directory

app = Flask(__name__)

options = config.configuration()

ILLEGAL_CHARS = ["//", "~", ".."]
DOCROOT = options.DOCROOT


@app.route("/")
def hello():
    return "UOCIS docker demo!\n"


@app.route("/<filename>")
def get_page(filename):
    if any((char in filename) for char in ILLEGAL_CHARS):
        abort(403)
    if filename not in os.listdir(DOCROOT):
        abort(404)
    return send_from_directory(DOCROOT, filename), 200


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
