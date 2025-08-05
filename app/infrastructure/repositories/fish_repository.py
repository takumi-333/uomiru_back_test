import os
from app.domain.entities.fish import Fish
from app.domain.repositories.fish_repository import IFishRepository

class FishRepository(IFishRepository):
  def save(self, fish: Fish) -> str:
    path = f"./storage/fish/{fish.user_id}.png"
    with open(path, "wb") as f:
      f.write(fish.image_bytes)
    return path
  
  def load(self, user_id: str, path: str) -> Fish:
    if not os.path.exists(path):
      raise FileNotFoundError("Fish not found")
    
    with open(path, "rb") as f:
      return Fish(user_id, f.read())