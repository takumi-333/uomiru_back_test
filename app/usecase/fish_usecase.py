from app.domain.repositories.fish_repository import IFishRepository
from app.domain.entities.fish import Fish
from app.services.fish_manager import generate_image, evolve_image

class FishUsecase:
  def __init__(self, fish_repo: IFishRepository):
    self.fish_repo = fish_repo
  
  def generate_fish(self, user_id: str, ans: str) -> bytes:
    img_bytes = generate_image(ans)
    fish = Fish(user_id, img_bytes)
    self.fish_repo.save(fish)
    return img_bytes

  def evolve_fish(self, user_id: str, id: str) -> bytes:
    my_fish = self.fish_repo.load(user_id)
    evolved_fish_img = evolve_image(my_fish.image_bytes, id)
    new_fish = Fish(user_id, evolved_fish_img)
    self.fish_repo.save(new_fish)
    return evolved_fish_img
  
  def get_fish_by_user_id(self, user_id: str) ->bytes:
    my_fish = self.fish_repo.load(user_id)
    return my_fish.image_bytes