# external library
import sqlalchemy as sa
import sqlalchemy.orm as so
# local imports
from my_app import app, db
from my_app.models import Category, Product

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'Category': Category, 'Product': Product}
