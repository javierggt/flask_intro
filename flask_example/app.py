#!/usr/bin/env python

"""
"""

from flask import Flask

from mica.archive import obspar


app = Flask('flask_tutorial')


# not adding a trailing slash will cause the route to no be matched with URLs with it
@app.route('/obspar/', methods=['GET'])
def get_obspar():
    """
    Service to return observation parameters.
    """
    pars = obspar.get_obspar(8008)

    return {'obspar': pars}, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
