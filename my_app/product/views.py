from werkzeug.exceptions import abort
from flask import Blueprint, render_template
from my_app.product.models import PRODUCTS

product_blueprint = Blueprint('product', __name__)


@product_blueprint.route('/product/<key>')
def product(key):
    product = PRODUCTS.get(key)
    if not product:
        abort(404)
    return render_template('product.html', product=product)

