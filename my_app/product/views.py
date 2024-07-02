from flask import Blueprint
from my_app.product.models import PRODUCTS

product = Blueprint('product', __name__)

@product.route('/')
def hello():
    return PRODUCTS['iphone']['name']