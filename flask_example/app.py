#!/usr/bin/env python

"""
"""

from flask import Flask, request
from flask_restful import reqparse

from mica.archive import obspar

app = Flask('flask_tutorial')


# not adding a trailing slash will cause the route to no be matched with URLs with it
@app.route('/obspar/', methods=['GET'])
def get_obspar():
    """
    Service to return observation parameters.
    """
    # unfortunately deprecated (https://flask-restful.readthedocs.io/en/latest/reqparse.html)
    # but I use it.
    # parser = reqparse.RequestParser()
    # parser.add_argument('obsid', help='ID of the observation', type=int, default=0)
    # args = parser.parse_args()
    # obsid = args.obsid
    obsid = int(request.form.get('obsid', request.values.get('obsid', 0)))
    pars = obspar.get_obspar(obsid)

    return {'obspar': pars}, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
