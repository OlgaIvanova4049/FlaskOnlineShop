from app.orm.models.user.user_model import UserModel
from app.orm.repository.base import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = UserModel

