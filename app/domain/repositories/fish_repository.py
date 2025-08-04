from abc import ABC, abstractmethod
from app.domain.entities.fish import Fish

class IFishRepository(ABC):
  @abstractmethod
  def save(self, fish: Fish) -> str:
    pass

  @abstractmethod
  def load(self, user_id: str) -> Fish:
    pass