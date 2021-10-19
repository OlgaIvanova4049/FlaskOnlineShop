from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, validates
from app.orm.models.base import BaseIDModel


class UserModel(BaseIDModel):
    __tablename__ = 'usr_user'

    email = Column(String, nullable=False)
    _password = Column(String, nullable=False)
    admin = Column(Boolean, default=False)
    order_list = relationship('OrderModel', back_populates='user', cascade="all, delete")

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError("failed email validation")
        return email

    # TODO хэш пароля

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password_text):
        self._password = hash(password_text)

