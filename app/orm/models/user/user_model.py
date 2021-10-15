from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship, validates
from orm.models.base import BaseIDModel

class UserModel(BaseIDModel):
    __tablename__ = 'usr_user'

    email = Column(String)
    password = Column(String)
    admin = Column(Boolean, default=False)

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError("failed email validation")
        return email

    order_list = relationship('OrderModel', back_populates='user', cascade="all, delete")

# TODO хэш пароля
    def __init__(self, email, password):
        self.email = email
        self.password = hash(password)
