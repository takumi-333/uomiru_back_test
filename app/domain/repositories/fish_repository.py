from abc import ABC, abstractmethod
from app.domain.entities.fish import Fish

class IFishRepository(ABC):
  @abstractmethod
  def create(self, fish: Fish) -> bool:
    pass

  @abstractmethod
  def find_by_user_id(self, user_id: str) -> Fish | None:
    pass