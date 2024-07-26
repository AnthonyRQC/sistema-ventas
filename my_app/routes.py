from flask import render_template, flash, redirect
from my_app import app
from my_app.forms import CategoryForm, LoginForm
from my_app.product.models import PRODUCTS

@app.route('/')
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
    form = LoginForm()
    if form.validate_on_submit():
        flash('User requested {}, password={}'.format(
            form.username.data, form.password.data))
        return redirect('/')
    return render_template('login.html', form=form)

@app.route('/register')
def new_user():
    return render_template('new_user.html')

@app.route('/sale')
def sale():
    return render_template('sale.html')
