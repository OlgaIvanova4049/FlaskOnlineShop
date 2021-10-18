from orm.models.base import BaseIDModel
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class CategoryModel(BaseIDModel):
    __tablename__ = "prd_category"

    name = Column(String, unique=True, nullable=False)
    parent_category = Column(Integer, ForeignKey('prd_category.id', ondelete='SET NULL'))

    product = relationship('ProductModel', back_populates='category')
    nested_categories = relationship('CategoryModel', remote_side='CategoryModel.id', uselist=True)
