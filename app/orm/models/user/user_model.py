from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, validates
from app.orm.models.base import BaseIDModel
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(BaseIDModel):
    __tablename__ = 'usr_user'

    email = Column(String, nullable=False, unique=True)
    _password = Column(String, nullable=False)
    admin = Column(Boolean, default=False)
    order_list = relationship('OrderModel', back_populates='user', cascade="all, delete")
    cart = relationship('CartModel', lazy="joined", uselist=False)
    token = relationship('TokenModel', lazy="joined", backref="user")


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
        self._password = generate_password_hash(password_text)

    def verify_password(self, password_text):
        return check_password_hash(self.password, password_text)

    def __repr__(self):
        return(str(self.email))


