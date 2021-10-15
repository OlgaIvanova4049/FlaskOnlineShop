from orm.models.base import BaseIDModel
from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship, validates


class DiscountModel(BaseIDModel):
    __tablename__ = "dsc_discount"

    name = Column(String, unique=True)


class ProductDiscountModel(BaseIDModel):
    __tablename__ = "dsc_product_discount"

    product_id = Column(Integer, ForeignKey('prd_product.id', ondelete='SET NULL'))
    discount_id = Column(Integer, ForeignKey('dsc_discount.id', ondelete='SET NULL'))
    amount = Column(Float)
    product = relationship('ProductModel', back_populates='product_discount')

    @validates('amount')
    def validate_(self, key, amount):
        if amount < 0:
            raise ValueError("set the correct value")
        return amount
