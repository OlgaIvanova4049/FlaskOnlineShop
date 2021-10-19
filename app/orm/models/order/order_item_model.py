from app.orm.models.base import BaseIDModel
from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship


class OrderItemModel(BaseIDModel):
    __tablename__ = "ord_order_item"
    __table_args__ = (
        CheckConstraint('price >= 0'),
        CheckConstraint('quantity >= 0')
    )

    order_id = Column(Integer, ForeignKey('ord_order.id'), ondelete='SET NULL')
    product_id = Column(Integer, ForeignKey('prd_product.id', ondelete='SET NULL'))
    price = Column(Integer, nullable=False)
    quantity = Column(Integer)
    product = relationship('ProductModel')

