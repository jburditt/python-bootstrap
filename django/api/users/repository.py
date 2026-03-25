from django.db.models.manager import BaseManager
from typing import Optional, List
from .models import User
from django.core.exceptions import ObjectDoesNotExist

class UserRepository:
  """Repository for User model database operations."""

  def __init__(self, db: BaseManager[User]):
    self.db = db
    
  def get_all_users(self) -> List[User]:
    return list(self.db.all())

  def get_user_by_id(self, user_id: int) -> Optional[User]:
    try:
      return self.db.get(User, id=user_id)
    except ObjectDoesNotExist:
      return None

  def create_user(self, username: str, email: str, first_name: str, last_name: str, role: int) -> User:
    return self.db.create(
      username=username,
      email=email,
      first_name=first_name,
      last_name=last_name,
      role=role
    )

  def update_user(self, user_id: int, **kwargs) -> Optional[User]:
    user = self.db.get_user_by_id(self, user_id)
    if not user:
      return None
    for key, value in kwargs.items():
      setattr(user, key, value)
    user.save()
    return user

  def delete_user(self, user_id: int) -> bool:
    user = self.db.get_user_by_id(self, user_id)
    if not user:
      return False
    user.delete()
    return True

