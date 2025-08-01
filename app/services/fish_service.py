from rembg import remove
from app.models.user_model import save_user_fish_path
from app.services.user_service import get_user_by_id
import os

def generate_fish(ans) -> bytes:
  # 将来的に生成AIを呼び出す処理へと変更
  with open("./static/fish.png",  "rb") as f:
    fish_data = f.read()
  return remove(fish_data)

def evolve_fish(target_img, feed_id) -> bytes:
  # 将来的に生成AIによって進化する処理
  if (feed_id == "chouchin"):
    fish_path = "./static/fish2.png"
  elif (feed_id == "clownfish"):
    fish_path = "./static/fish3.png"
  elif (feed_id == "shark"):
    fish_path = "./static/fish4.png"
  else:
    fish_path = ""
  if fish_path != "":
    with open(fish_path, "rb") as f:
      fish_data = f.read()
  else:
    fish_data = target_img
  return fish_data

def save_fish_image(user_id: str, fish_img: bytes) -> str:
  fish_path = f"./storage/fish/{user_id}.png"
  with open(fish_path, "wb") as f:
    f.write(fish_img)
  save_user_fish_path(user_id, fish_path)
  return fish_path
  
def generate_fish_image(user_id, ans):
  result = generate_fish(ans)
  save_fish_image(user_id, result)
  return result

def evolve_fish_image(user_id, feed_id):
  user_data = get_user_by_id(user_id)
  print(user_data)
  target_img = get_fish_by_path(user_data["my_fish_path"])
  result = evolve_fish(target_img, feed_id)
  save_fish_image(user_id, result)
  return result

def get_fish_by_path(path):
  if not os.path.exists(path):
    return None
  with open(path, "rb") as f:
    return f.read()
