from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class CategoryForm(FlaskForm):
    category = StringField('Category Name',validators=[DataRequired()])
    details = StringField('Details', validators=[DataRequired()])
    submit = SubmitField('Create Category')