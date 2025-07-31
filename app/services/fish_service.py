from rembg import remove
from app.models.user_model import save_user_fish_path
import os

def generate_fish(ans) -> bytes:
  # 将来的に生成AIを呼び出す処理へと変更
  with open("./static/fish.png",  "rb") as f:
    fish_data = f.read()
  return remove(fish_data)

def save_fish_image(user_id: str, fish_img: bytes) -> str:
  fish_path = f"./mock_db/fish/{user_id}.png"
  with open(fish_path, "wb") as f:
    f.write(fish_img)
  save_user_fish_path(user_id, fish_path)
  return fish_path
  
def generate_fish_image(user_id, ans):
  result = generate_fish(ans)
  save_fish_image(user_id, result)
  return result

def evolve_fish_image(target_img, feed_img, feed_data):
  with open("./static/fish2.png", "rb") as f:
    base = f.read()
  return remove(base)

def get_fish_by_path(path):
  if not os.path.exists(path):
    return None
  with open(path, "rb") as f:
    return f.read()
