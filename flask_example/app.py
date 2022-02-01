#!/usr/bin/env python

"""
"""

from flask import Flask


from obspar import blueprint as obspar
from root import blueprint as root


if __name__ == "__main__":
    app = Flask('flask_tutorial')
    app.register_blueprint(obspar)
    app.register_blueprint(root)
    app.run(host='0.0.0.0', debug=True, port=5000)
