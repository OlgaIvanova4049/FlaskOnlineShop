from app.orm.models.base import BaseIDModel
from sqlalchemy import Column, Integer, Float, ForeignKey, String, CheckConstraint
from sqlalchemy.orm import relationship


class DiscountModel(BaseIDModel):
    __tablename__ = "dsc_discount"

    name = Column(String, unique=True)


class ProductDiscountModel(BaseIDModel):
    __tablename__ = "dsc_product_discount"
    __table_args__ = (
        CheckConstraint('amount >= 0'),
    )

    product_id = Column(Integer, ForeignKey('prd_product.id', ondelete='SET NULL'))
    discount_id = Column(Integer, ForeignKey('dsc_discount.id', ondelete='SET NULL'))
    amount = Column(Float)
    product = relationship('ProductModel', back_populates='product_discount')

