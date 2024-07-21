from datetime import datetime, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so
from my_app import db
# python module to make optional a column
from typing import Optional

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
    stock: so.Mapped[int]
    purchase_price: so.Mapped[float]
    selling_price: so.Mapped[float]
    description: so.Mapped[Optional[str]] = so.mapped_column(sa.String(120))
    created_at: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    category_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Category.id),
                                               index=True)
    category: so.Mapped[Category] = so.relationship(back_populates='products')
    
    def __repr__(self):
        return '<Product {}>'.format(self.name)