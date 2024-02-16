from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    with app.app_context():
        @app.route('/')
        def home():
            return render_template("index.html")
        return app

