import datetime
from flask import Flask

def new_app():
    app = Flask(__name__)
    from . import routes
    app.register_blueprint(routes.bp)

    @app.template_filter('datetimeformat')
    def datetimeformat(value, format = '%Y-%m-%d'):
        return datetime.datetime.utcfromtimestamp(value).strftime(format)
    
    return app

    