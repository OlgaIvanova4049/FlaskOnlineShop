from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, validates
from app.orm.models.base import BaseIDModel


class UserModel(BaseIDModel):
    __tablename__ = 'usr_user'

    email = Column(String, nullable=False, unique=True)
    _password = Column(String, nullable=False)
    admin = Column(Boolean, default=False)
    order_list = relationship('OrderModel', back_populates='user', cascade="all, delete")
    cart = relationship('CartModel', lazy="joined", uselist=False)
    token = relationship('TokenModel', lazy="joined", uselist=False)


    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError("failed email validation")
        return email


    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password_text):
        self._password = hash(password_text)

    def __repr__(self):
        return(str(self.email))


