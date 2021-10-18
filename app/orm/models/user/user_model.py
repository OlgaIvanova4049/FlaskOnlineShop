from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship, validates
from orm.models.base import BaseIDModel


class UserModel(BaseIDModel):
    __tablename__ = 'usr_user'

    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    admin = Column(Boolean, default=False)
    order_list = relationship('OrderModel', back_populates='user', cascade="all, delete")

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError("failed email validation")
        return email

    # TODO хэш пароля
    def hash_password(self, password):
        self.password = hash(password)
        return self.password
