# external library
import sqlalchemy as sa
import sqlalchemy.orm as so
# local imports
# import database and flask app
from my_app import app, db
# import tables sqlalchemy
from my_app.models import Category, Product, Client, Invoice, Purchase, PurchaseDetail, Sale, SaleDetail, Suplier, User

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 
            'so': so, 
            'db': db, 
            'Category': Category, 
            'Product': Product,
            'Client': Client,
            'Invoice': Invoice,
            'Product': Product,
            'Purchase': Purchase,
            'PurchaseDetail': PurchaseDetail,
            'Sale': Sale,
            'SaleDetail': SaleDetail,
            'Suplier': Suplier,
            'User': User
            }
