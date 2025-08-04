from abc import ABC, abstractmethod
from app.domain.entities.user import User

class IUserRepository(ABC):
  @abstractmethod
  def create(self, user: User) -> bool:
    pass

  @abstractmethod
  def delete(self, user_id: str) -> bool:
    pass

  @abstractmethod
  def find_by_id(self, user_id: str) -> User | None:
    pass

  @abstractmethod
  def verify_password(self, user_id: str, password: str) -> bool:
    pass

  @abstractmethod
  def save_fish_path(self, user_id: str, path: str):
    pass