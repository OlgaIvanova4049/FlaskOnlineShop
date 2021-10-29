from sqlalchemy.ext.hybrid import hybrid_property

from app.orm.models.base import BaseIDModel
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class CategoryModel(BaseIDModel):
    __tablename__ = "prd_category"

    name = Column(String, unique=True, nullable=False)
    parent_category = Column(Integer, ForeignKey('prd_category.id', ondelete='SET NULL'))

    product = relationship('ProductModel', back_populates='category')
    parent_object = relationship('CategoryModel', remote_side='CategoryModel.id', uselist=True)

    #TODO: many-to-one self reference
