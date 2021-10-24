from app.orm.models.user.token_model import TokenModel
from app.orm.repository.base import BaseRepository


class TokenRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = TokenModel