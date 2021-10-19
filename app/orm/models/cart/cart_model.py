from app.orm.models.base import BaseIDModel
from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship


class CartModel(BaseIDModel):
    __tablename__ = "crt_cart"
    __table_args__ = (
        CheckConstraint('total_price >= 0'),
    )

    user_id = Column(Integer, ForeignKey('usr_user.id', ondelete='SET NULL'))
    total_price = Column(Integer, CheckConstraint('total_price>=0'), default=0)
    cart_item = relationship('CartItemModel', cascade="all, delete")

