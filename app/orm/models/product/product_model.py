from select import select

from sqlalchemy.ext.hybrid import hybrid_property

from app.orm.models.base import BaseIDModel
from sqlalchemy import Column, Integer, ForeignKey, String, Text, CheckConstraint, func
from sqlalchemy.orm import relationship

from app.orm.models.discount.discount import ProductDiscountModel


class ProductModel(BaseIDModel):
    __tablename__ = "prd_product"
    __table_args__ = (
        CheckConstraint('price >= 0'),
        CheckConstraint('quantity >= 0')
    )

    name = Column(String, unique=True, nullable=False)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey('prd_category.id', ondelete='SET NULL'))
    quantity = Column(Integer)
    price = Column(Integer, nullable=False)
    category = relationship('CategoryModel', back_populates='product')
    product_discount = relationship('ProductDiscountModel', back_populates='product')

    @hybrid_property
    def total_discount(self):
        return sum(discount.amount for discount in self.product_discount)

    @total_discount.expression
    def total_discount(cls):
        return select(func.sum(ProductDiscountModel.amount)).where(
            ProductDiscountModel.product_id == cls.id).label(
            'total_discount')
