from django.db.models.manager import BaseManager
from .services.base_repository import Repository
from .models import User

class UserRepository(Repository):
  """Repository for User model database operations."""

  def __init__(self, db: BaseManager[User]):
    super().__init__(db)
    self.db = db
