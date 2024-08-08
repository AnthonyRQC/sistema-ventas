from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DecimalField
# validators in forms Email validator needs install email-validator
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
# importamos la base de datos para verificar duplicaciones de usuarios o emails
import sqlalchemy as sa
from my_app import db
from my_app.models import User

class CategoryForm(FlaskForm):
    category = StringField('Category Name',validators=[DataRequired()])
    details = StringField('Details', validators=[DataRequired()])
    submit = SubmitField('Create Category')
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('LogIn')
    
class RegisterForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    docnumber = IntegerField('Document Number', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    email = StringField('Email Adress', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # Func EqualTo para comprobar typos en la contraseña
    password2 = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    # WTForms take validate_<field_name> and add this to stock validators
    def validate_username(self, username):
        # al usar scalar y no scalars nos devolvera solo un resultado
        user = db.session.scalar(sa.select(User).where(
            User.user_name == username.data))
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('Please use a different email address.')
    
