from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import create_engine

class Sqlachemy:
    database_engine = create_engine(settings.sqlalchemy_database_uri, echo=True)

db = Sqlachemy()