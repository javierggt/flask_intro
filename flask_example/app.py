#!/usr/bin/env python

"""
"""


import werkzeug.exceptions
from flask import Flask, render_template

from cmds_validate import blueprint as cmds_validate
from obspar import blueprint as obspar
from root import blueprint as root


def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app = Flask('flask_tutorial')
    app.register_error_handler(werkzeug.exceptions.NotFound, page_not_found)
    app.register_blueprint(obspar, url_prefix='/obspar')
    app.register_blueprint(cmds_validate, url_prefix='/cmds_validate')
    app.register_blueprint(root)
    app.run(host='0.0.0.0', debug=True, port=5000)
