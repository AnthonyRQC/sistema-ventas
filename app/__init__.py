from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    with app.app_context():
        # Una vez creamos la app llamamos el blueprint que necesitamos
        # llamamos el plueprint intro creado en intro/__init__
        from . import intro
        app.register_blueprint(intro.intro_bp)
        # cada vez que se inicia la aplicacion esta devuelve
        # la app creada en flask
        return app
