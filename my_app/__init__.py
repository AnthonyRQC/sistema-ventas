from flask import Flask
#python config and secretkey
from config import Config
from my_app.product.views import product_blueprint

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(product_blueprint)

from my_app import routes
