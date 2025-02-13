from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123Summer 321Summer'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefi='/')
    app.register_blueprint(auth, url_prefi='/')

    return app