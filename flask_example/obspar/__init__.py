#!/usr/bin/env python

"""
"""

from flask import Blueprint, render_template, abort
from flask_restful import reqparse
import werkzeug

from mica.archive import cda

blueprint = Blueprint('obspar', __name__, template_folder='templates')


@blueprint.route('/api', methods=['GET'])
def get_obspar():
    """
    Service to return observation parameters.
    """
    try:
        parser = reqparse.RequestParser()
        parser.add_argument('obsid', help='ID of the observation', type=int, default=0)
        args = parser.parse_args()
        pars = cda.get_ocat_local(obsid=args.obsid)
        if len(pars) == 0:
            return ({
                'error': f'No OBSID {args.obsid}',
                'obspar': {}
            }, 404)

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
    pars = cda.get_ocat_local(obsid=args.obsid)
    if len(pars) == 0:
        abort(404)
        # return render_template('404.html')

    return render_template('obspar.html', pars=pars)
