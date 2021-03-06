from app.orm.models.base import BaseIDModel
from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint, Index
from sqlalchemy.orm import relationship


class CartItemModel(BaseIDModel):
    __tablename__ = "crt_cart_item"
    __table_args__ = (
        CheckConstraint('price >= 0'),
        CheckConstraint('quantity >= 0'),
        Index('product_in_cart', "cart_id", "product_id")
    )

    cart_id = Column(Integer, ForeignKey('crt_cart.id', ondelete='SET NULL'))
    product_id = Column(Integer, ForeignKey('prd_product.id', ondelete='SET NULL'))
    price = Column(Integer, nullable=False)
    quantity = Column(Integer)
    product = relationship('ProductModel', lazy="joined")
