from flask import Blueprint, url_for

blueprint = Blueprint('root', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET'])
def root():
    """
    Root page.
    """
    text = f"""
    <html>
        <body>
            <h1>OBSPAR Service<h1>

            <a href="{url_for('obspar.view_obspar')}?obsid=8008"> Check this out </a>
        </body>
    </html>
    """
    return text
