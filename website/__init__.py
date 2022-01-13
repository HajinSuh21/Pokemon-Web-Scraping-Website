from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'key'

    from .scraping import sets
    from .views import views

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(sets, url_prefix='/')

    return app