import flask

from . import db_session # когда точка пробел это в этой директории
from .news import News # когда точка без пробела это другая директория
blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)

@blueprint.route('/api/news')
def get_news():
    return 'API news_api работает'