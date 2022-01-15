from flask import Flask

def create_app():
    app = Flask(__name__)
    from .scraping import sets
    app.register_blueprint(sets, url_prefix='/')
    return app
