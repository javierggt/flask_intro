#!/usr/bin/env python

"""
"""

from flask import Blueprint
from flask_restful import reqparse

from mica.archive import obspar

blueprint = Blueprint('obspar', __name__)

# not adding a trailing slash will cause the route to no be matched with URLs with it
@blueprint.route('/obspar/', methods=['GET'])
def get_obspar():
    """
    Service to return observation parameters.
    """
    parser = reqparse.RequestParser()
    parser.add_argument('obsid', help='ID of the observation', type=int, default=0)
    args = parser.parse_args()
    pars = obspar.get_obspar(args.obsid)

    return {'obspar': pars}, 200
