#!/usr/bin/env python

"""
"""

from flask import Blueprint, render_template, jsonify, abort
from flask_restful import reqparse
import werkzeug

from mica.archive import obspar

blueprint = Blueprint('obspar', __name__, template_folder='templates')


OBSERVATIONS = [8007, 8008]


@blueprint.route('/api/observations', methods=['GET'])
def get_observations():
    """
    Service to return observation parameters.
    """
    return jsonify(OBSERVATIONS), 200


@blueprint.route('/api', methods=['GET'])
def get_obspar():
    """
    Service to return observation parameters.
    """
    try:
        parser = reqparse.RequestParser()
        parser.add_argument('obsid', help='ID of the observation', type=int, default=0)
        args = parser.parse_args()
        if args.obsid not in OBSERVATIONS:
            return ({
                'error': f'No OBSID {args.obsid}',
                'obspar': {}
            }, 404)
        pars = obspar.get_obspar(args.obsid)
        if pars is None:
            pars = {}
    except werkzeug.exceptions.BadRequest as e:
        return {'error': str(e), 'obspar': {}}, 400

    return {'obspar': pars}, 200


@blueprint.route('/', methods=['GET'])
def view_obspar():
    """
    View observation parameters.
    """
    parser = reqparse.RequestParser()
    parser.add_argument('obsid', help='ID of the observation', type=int, default=0)
    args = parser.parse_args()
    pars = obspar.get_obspar(args.obsid)
    if args.obsid not in OBSERVATIONS:
        abort(404)
        # return render_template('404.html')

    if pars is None:
        pars = {}

    return render_template('obspar.html', data={'obsid': args.obsid, 'pars': pars})
