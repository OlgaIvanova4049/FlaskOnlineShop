from app.orm.models.user.scope_model import RoleModel
from app.orm.repository.base import BaseRepository, session_scope


class RoleRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = RoleModel

    def define_scope(self, role_id):
        with session_scope() as session:
            role = session.query(self.model).get(role_id)
            scopes = role.scopes
            scopes_name = [scope.name for scope in scopes]
            return scopes_name
