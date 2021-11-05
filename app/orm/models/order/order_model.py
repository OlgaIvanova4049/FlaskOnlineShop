from app.orm.models.base import BaseIDModel
from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship


class OrderModel(BaseIDModel):
    __tablename__ = "ord_order"
    __table_args__ = (
        CheckConstraint('total_price >= 0'),
    )

    user_id = Column(Integer, ForeignKey('usr_user.id', ondelete='SET NULL'))
    total_price = Column(Integer)
    user = relationship('UserModel', back_populates='order_list')
    order_items = relationship('OrderItemModel', lazy="joined", cascade="all, delete")
