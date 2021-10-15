from orm.models.base import BaseIDModel
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, validates


class CartItemModel(BaseIDModel):
    __tablename__ = "crt_cart_item"

    cart_id = Column(Integer, ForeignKey('crt_cart.id', ondelete='SET NULL'))
    product_id = Column(Integer, ForeignKey('prd_product.id', ondelete='SET NULL'))
    price = Column(Integer, nullable=False)
    quantity = Column(Integer)
    product = relationship('ProductModel')

    @validates('price')
    def validate_(self, key, price):
        if price <= 0:
            raise ValueError("set the correct value")
        return price

    @validates('quantity')
    def validate_(self, key, quantity):
        if quantity < 0:
            raise ValueError("set the correct value")
        return quantity


