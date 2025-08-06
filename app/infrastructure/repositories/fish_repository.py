import os
from app.domain.entities.fish import Fish
from app.domain.repositories.fish_repository import IFishRepository
from app.infrastructure.db.models import FishModel
from app.infrastructure.db.base import db

class FishRepository(IFishRepository):
  def create(self, fish: Fish) -> bool:
    model = FishModel(
      img_path=fish.img_path,
      size=fish.size,
      user_id=fish.user_id
    )
    db.session.add(model)
    db.session.commit()
    return True
  
  def find_by_user_id(self, user_id: str) -> Fish | None:
    model = FishModel.query.filter_by(user_id=user_id).first()
    if not model:
      return None
    return Fish(
      id=model.id,
      img_path=model.img_path,
      size=model.size,
      user_id=model.user_id
    )
    