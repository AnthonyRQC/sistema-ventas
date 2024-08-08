from flask import Flask
#python config and secretkey outside my_app
from config import Config
from flask_sqlalchemy import SQLAlchemy
# libreria externa instalada por recomendacion de un tutorial
from flask_migrate import Migrate
from flask_login import LoginManager

from my_app.product.views import product_blueprint

app = Flask(__name__)
# agregando el archivo de config al proyecto
app.config.from_object(Config)
# iniciando la base de datos
db = SQLAlchemy(app)
# usando la libreria migrate
migrate = Migrate(app, db)
# create login in app
login = LoginManager(app)
# esta funcion es donde redirige la aplicacion si el usuario no esta logeado con @login_required
login.login_view = 'login'

app.register_blueprint(product_blueprint)

from my_app import routes, models, errors
