from app.domain.repositories.fish_repository import IFishRepository
from app.domain.entities.fish import Fish
from app.services.fish_manager import generate_image, evolve_image, save_fish_image, load_fish_image

class FishUsecase:
  def __init__(self, fish_repo: IFishRepository):
    self.fish_repo = fish_repo
  
  def generate_fish(self, user_id: str, ans: str) -> bytes:
    img_bytes = generate_image(ans)
    img_path = f"./storage/fish/{user_id}.png"
    save_fish_image(img_bytes=img_bytes, path=img_path)
    newFish = Fish(
      img_path=img_path,
      size=1,
      user_id=user_id
    )
    self.fish_repo.create(newFish)
    return img_bytes

  def evolve_fish(self, user_id: str, id: str) -> bytes:
    fish = self.fish_repo.find_by_user_id(user_id)
    my_fish_img = load_fish_image(fish.img_path)
    evolved_fish_img = evolve_image(my_fish_img, id)
    # size upの処理とか入れてもいいかも
    save_fish_image(evolved_fish_img, fish.img_path)
    return evolved_fish_img
  
  def get_fish_by_user_id(self, user_id: str) -> bytes:
    fish = self.fish_repo.find_by_user_id(user_id)
    my_fish = load_fish_image(fish.img_path)
    return my_fish