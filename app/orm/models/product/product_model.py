from orm.models.base import BaseIDModel
from sqlalchemy import Column, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship, validates, sessionmaker


class ProductModel(BaseIDModel):
    __tablename__ = "prd_product"

    name = Column(String, unique=True)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey('prd_category.id', ondelete='SET NULL'))
    quantity = Column(Integer)
    price = Column(Integer, nullable=False)
    category = relationship('CategoryModel', back_populates='product')
    product_discount = relationship('ProductDiscountModel', back_populates='product')

    @validates('price')
    def validate_(self, key, price):
        if price <= 0:
            raise ValueError("set the correct value")
        return price

    @validates('quantity')
    def validate_(self, key, quantity):
        if quantity < 0:
            raise ValueError("set the correct value")
        return quantity

    @staticmethod
    def total_discount():
        Session = sessionmaker()
        session = Session()
        discounts = session.query(ProductModel.product_discount).all()
        return sum([discount.amount for discount in discounts])

    total_discount = total_discount()
