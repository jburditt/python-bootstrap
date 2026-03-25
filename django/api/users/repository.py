from typing import Optional, List
from .models import User
from django.core.exceptions import ObjectDoesNotExist

class UserRepository:
    """Repository for User model database operations."""

    @staticmethod
    def get_all_users() -> List[User]:
        return list(User.objects.all())

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        try:
            return User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create_user(username: str, email: str, first_name: str, last_name: str, role: int) -> User:
        return User.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=role
        )

    @staticmethod
    def update_user(user_id: int, **kwargs) -> Optional[User]:
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            return None
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
        return user

    @staticmethod
    def delete_user(user_id: int) -> bool:
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            return False
        user.delete()
        return True

