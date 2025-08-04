from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.feed import Feed

class IFeedRepository(ABC):
  @abstractmethod
  def get_all(self) -> List[Feed]:
    pass

  @abstractmethod
  def get_image_by_path(self, path: str) -> bytes | None:
    pass