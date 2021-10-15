from orm.models.base import BaseIDModel
from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship, validates


class CartModel(BaseIDModel):
    __tablename__ = "crt_cart"

    user_id = Column(Integer, ForeignKey('usr_user.id', ondelete='SET NULL'))
    total_price = Column('total_price', Integer, CheckConstraint('total_price>=0'), default=0)
    cart_item = relationship('CartItemModel', cascade="all, delete")

    @validates('total_price')
    def validate_(self, key, total_price):
        if total_price <= 0:
            raise ValueError("set the correct value")
        return total_price
