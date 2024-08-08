from datetime import datetime, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so
from my_app import db
# python module to make optional a column
from typing import Optional
# seguridad a las contraseñas
from werkzeug.security import generate_password_hash, check_password_hash
# mixins para dar implementacion a la clase usuario como autenticaciones, anonimos, activdad y otros
from flask_login import UserMixin
# importando de my_app init el login agregado a la aplicacion
from my_app import login

# funcion para poder mantener el log de un usario en base a su id 
@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

# Category table
class Category(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    details: so.Mapped[Optional[str]] = so.mapped_column(sa.String(120))
    products: so.WriteOnlyMapped['Product'] = so.relationship(
        back_populates='category')
    
    def __repr__(self):
        return '<Category {}>'.format(self.name)
    
    
    
class Product(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(60))
    stock: so.Mapped[Optional[int]]
    purchase_price: so.Mapped[Optional[float]]
    selling_price: so.Mapped[Optional[float]]
    description: so.Mapped[Optional[str]] = so.mapped_column(sa.String(120))
    created_at: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    category_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Category.id),
                                               index=True)
    category: so.Mapped[Category] = so.relationship(back_populates='products')
    
    def __repr__(self):
        return '<Product {}>'.format(self.name)
    
class Client(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    document_number: so.Mapped[Optional[int]]
    first_name: so.Mapped[str] = so.mapped_column(sa.String(64))
    last_name: so.Mapped[str] = so.mapped_column(sa.String(64))
    email: so.Mapped[Optional[str]] = so.mapped_column(sa.String(120))
    phone_number: so.Mapped[Optional[int]]
    state: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    created_at: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return '<Client first name{}, last name{}>'.format(self.first_name, self.last_name)
    
# agregando usermixin a la tabla usuarios
class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    user_name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    password: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    document_number: so.Mapped[Optional[int]]
    first_name: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    last_name: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    email: so.Mapped[Optional[str]] = so.mapped_column(sa.String(120), index=True, unique=True)
    state: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    created_at: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    def set_password(self, form_password):
        self.password = generate_password_hash(form_password)
    
    def check_password(self, form_password):
        return check_password_hash(self.password, form_password)
    
    def __repr__(self):
        return '<User first name{}, last name{}>'.format(self.first_name, self.last_name)
    
class Sale(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    # para poder acceder a User y Client objects directamente desde Sale y vice versa
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id),
                                               index=True)
    user: so.Mapped[User] = so.relationship(User)
    client_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Client.id),
                                               index=True)
    client: so.Mapped[Client] = so.relationship(Client)
    # columnas normales de la tabla
    client_doc_number: so.Mapped[Optional[int]]
    client_doc_name: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    recived_money: so.Mapped[Optional[float]]
    change_money: so.Mapped[Optional[float]]
    total_amount_sale: so.Mapped[Optional[float]]
    created_at: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    def __repr__(self):
        return '<Sale recieved money{}, change money{}>'.format(self.recived_money, self.change_money)
    
class SaleDetail(db.Model):
    __tablename__ = "sale_detail"
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    sale_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Sale.id), index=True)
    product_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Product.id), index=True)
    price_sale:so.Mapped[float]
    quantity: so.Mapped[int]
    sub_total:so.Mapped[float]
    created_at: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    
class Suplier(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    document: so.Mapped[int]
    email: so.Mapped[Optional[str]] = so.mapped_column(sa.String(120))
    phone_number: so.Mapped[int]
    state: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    created_at: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    
class Purchase(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)
    suplier_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Suplier.id), index=True)
    document_number: so.Mapped[int]
    document_type: so.Mapped[str] = so.mapped_column(sa.String(64))
    total_amount_sale: so.Mapped[float]
    created_at: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return '<purchase document number{}, document type{}>'.format(self.document_number, self.document_type)
    
class PurchaseDetail(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    purchase_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Purchase.id), index=True)
    product_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Product.id), index=True)
    purchase_price:so.Mapped[float]
    sale_price:so.Mapped[float]
    quantity: so.Mapped[int]
    total:so.Mapped[float]
    created_at: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    
class Invoice(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    sale_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Sale.id), index=True)
    total_amount_sale: so.Mapped[float]
    payment_method: so.Mapped[str] = so.mapped_column(sa.String(64))
    invoice_date: so.Mapped[datetime]
    created_at: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))