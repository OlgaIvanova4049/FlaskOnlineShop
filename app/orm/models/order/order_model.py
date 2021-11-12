from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.orm.models.base import BaseIDModel


class OrderModel(BaseIDModel):
    __tablename__ = "ord_order"
    __table_args__ = (CheckConstraint("total_price >= 0"),)

    user_id = Column(Integer, ForeignKey("usr_user.id", ondelete="SET NULL"))
    total_price = Column(Integer)
    user = relationship("UserModel", lazy="joined")
    order_items = relationship(
        "OrderItemModel", lazy="joined", cascade="all, delete"
    )
