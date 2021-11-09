from app.orm.models.user.scope_model import usr_role_scope, RoleModel, ScopeModel
from app.orm.repository.base import BaseRepository, session_scope


class ScopeRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = ScopeModel

def define_scope(role_id):
    with session_scope() as session:
        role = session.query(RoleModel).get(role_id)
        scopes = role.scopes
        scopes_name = [scope.name for scope in scopes]
        return scopes_name
