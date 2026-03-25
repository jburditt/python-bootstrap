from django.db.models.manager import BaseManager
from typing import Optional, List
from .services.base_repository import Repository
from .models import User
from django.core.exceptions import ObjectDoesNotExist

class UserRepository(Repository):
  """Repository for User model database operations."""

  def __init__(self, db: BaseManager[User]):
    super().__init__(db)
    self.db = db
