from orm.models.base import BaseIDModel
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, validates


class OrderModel(BaseIDModel):
    __tablename__ = "ord_order"

    user_id = Column(Integer, ForeignKey('usr_user.id', ondelete='SET NULL'))
    total_price = Column(Integer)
    user = relationship('UserModel', back_populates='order_list')

    @validates('total_price')
    def validate_(self, key, total_price):
        if total_price < 0:
            raise ValueError("set the correct value")
        return total_price
