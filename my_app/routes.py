from flask import render_template, flash, redirect, url_for
from my_app import app
from my_app.forms import CategoryForm, LoginForm, RegisterForm
from my_app.product.models import PRODUCTS
# import para el funcioamiento de login y la base de datos
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from my_app import db
from my_app.models import User
# en esta variable flask guarda las request del usuario 
from flask import request

from urllib.parse import urlsplit

@app.route('/')
@app.route('/home')
@login_required
def home():
    return render_template('home.html', products=PRODUCTS)

@app.route('/add_categ', methods=['GET', 'POST'])
def add_category():
    form = CategoryForm()
    if form.validate_on_submit():
        flash('Category requested {}, details={}'.format(
            form.category.data, form.details.data))
        return redirect('/')
    return render_template('add_category.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # this two lines is if loged user wants to navigate /login page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit(): 
        user = db.session.scalar(
            sa.select(User).where(User.user_name == form.username.data)
        )
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            print('not loged')
            return redirect(url_for('login'))
        # login_user from flask-login will register the currrent_user in next navigates
        print('loged')
        login_user(user, remember=form.remember_me.data)
        # aqui ponemos next_page donde se guarda la pagina que se queria acceder antes del login
        # por defecto si no hay una pagina se mandara a home
        # se toma la ilnformacion tomada del cliente con request 
        next_page = request.args.get('next')
        # si request no tiene un next argument o si esta tiene un nombre de domino comopleto esta se ignora
        # el segundo or es mas por seguridad solo aceptando url relativos y no absolutos
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)      
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    # func from flask-login
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    # estas lineas no nos sirven por que solo se puede registrar una vez iniciado por el admin
    #if current_user.is_authenticated:
    #    return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(user_name=form.username.data, 
                    email=form.email.data,
                    document_number=form.docnumber.data,
                    first_name=form.firstname.data,
                    last_name=form.lastname.data,
                    state=form.state.data,
                    )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('home'))
    return render_template('new_user.html', form=form)



@app.route('/sale')
def sale():
    return render_template('sale.html')
 