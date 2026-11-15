def create_app():
    app = ...

    from . import auth
    app.register_blueprint(auth.bp)
    return app