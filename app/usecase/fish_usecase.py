from app.domain.repositories.fish_repository import IFishRepository
from app.domain.repositories.user_repository import IUserRepository
from app.domain.entities.fish import Fish
from app.services.fish_manager import generate_image, evolve_image

class FishUsecase:
  def __init__(self, fish_repo: IFishRepository, user_repo: IUserRepository):
    self.fish_repo = fish_repo
    self.user_repo = user_repo
  
  def generate_fish(self, user_id: str, ans: str) -> bytes:
    img_bytes = generate_image(ans)
    fish = Fish(user_id, img_bytes)
    path = self.fish_repo.save(fish)
    self.user_repo.save_fish_path(user_id, path)
    return img_bytes

  def evolve_fish(self, user_id: str, id: str) -> bytes:
    user = self.user_repo.find_by_id(user_id)
    my_fish = self.fish_repo.load(user_id, user.my_fish_path)
    evolved_fish_img = evolve_image(my_fish.image_bytes, id)
    new_fish = Fish(user_id, evolved_fish_img)
    self.fish_repo.save(new_fish)
    return evolved_fish_img
  
  def get_fish_by_user_id(self, user_id: str) ->bytes:
    user = self.user_repo.find_by_id(user_id)
    my_fish = self.fish_repo.load(user_id, user.my_fish_path)
    return my_fish.image_bytes