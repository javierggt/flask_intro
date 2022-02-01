from flask import Blueprint, url_for

blueprint = Blueprint('root', __name__)


@blueprint.route('/', methods=['GET'])
def root():
    """
    Root page.
    """
    text = f"""
    <html>
        <body>
            <h1>OBSPAR Service<h1>

            <a href="{url_for('obspar.get_obspar')}?obsid=8008"> Check this out </a>
        </body>
    </html>
    """
    return text