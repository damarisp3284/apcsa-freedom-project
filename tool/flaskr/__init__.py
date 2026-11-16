import os
from flask import Flask, redirect, url_for

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    def create_app(test_config=None):
        app = Flask(__name__, instance_relative_config=True)
    return app

def create_app():
    app = ...
    # existing code omitted

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
