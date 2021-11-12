from sqlalchemy import (
    CheckConstraint,
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from app.orm.models.base import BaseIDModel


class ProductModel(BaseIDModel):
    __tablename__ = "prd_product"
    __table_args__ = (
        CheckConstraint("price >= 0"),
        CheckConstraint("quantity >= 0"),
    )

    name = Column(String, unique=True, nullable=False)
    description = Column(Text)
    category_id = Column(
        Integer, ForeignKey("prd_category.id", ondelete="SET NULL")
    )
    quantity = Column(Integer)
    price = Column(Integer, nullable=False)
    category = relationship(
        "CategoryModel", back_populates="product", uselist=False
    )
    product_discount = relationship(
        "ProductDiscountModel", back_populates="product"
    )

    @hybrid_property
    def total_discount(self):
        return sum(discount.amount for discount in self.product_discount)
