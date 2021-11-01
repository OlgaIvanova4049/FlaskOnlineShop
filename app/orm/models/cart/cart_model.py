import uuid as uuid

from app.orm.models.base import BaseIDModel
from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


class CartModel(BaseIDModel):
    __tablename__ = "crt_cart"
    __table_args__ = (
        CheckConstraint('total_price >= 0'),
    )

    user_id = Column(Integer, ForeignKey('usr_user.id', ondelete='SET NULL'))
    total_price = Column(Integer, CheckConstraint('total_price>=0'), default=0)
    uid = Column(UUID(as_uuid=True), default=uuid.uuid4, index=True)
    cart_item = relationship('CartItemModel', cascade="all, delete")

