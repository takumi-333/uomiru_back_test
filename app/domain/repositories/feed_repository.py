from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.feed import Feed

class IFeedRepository(ABC):
  @abstractmethod
  def get_all(self) -> List[Feed]:
    pass

  @abstractmethod
  def find_by_id(self, id: int) -> Feed:
    pass