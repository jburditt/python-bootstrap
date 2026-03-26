from django.db.models.manager import BaseManager
from typing import Optional, List, TypeVar
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
    
Entity = TypeVar("Entity", bound=models.Model)

class Repository:
  """Base Repository for model database operations."""

  def __init__(self, db: BaseManager[Entity]):
    self.db = db
    
  def all(self) -> List[Entity]:
    return list(self.db.all())

  def get(self, id: object) -> Optional[Entity]:
    try:
      return self.db.get(id=id)
    except ObjectDoesNotExist:
      return None

  def create(self, **kwargs) -> Entity:
    return self.db.create(**kwargs)

  def update(self, id: object, **kwargs) -> Optional[Entity]:
    user = self.db.get(id=id)
    if not user:
      return None
    for key, value in kwargs.items():
      setattr(user, key, value)
    user.save()
    return user

  def delete(self, id: object) -> bool:
    user = self.db.get(id=id)
    if not user:
      return False
    user.delete()
    return True

