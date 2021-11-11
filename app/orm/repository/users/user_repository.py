from app.orm.models.user.user_model import UserModel
from app.orm.repository.base import BaseRepository, session_scope


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = UserModel

    def find_by_email(self, email):
        with session_scope() as session:
            return session.query(self.model).filter_by(email=email).first()