from rembg import remove
import os
from app.domain.entities.feed import Feed

def generate_image(ans: str) -> bytes:
  # 仮の処理
  with open("./static/fish.png", "rb") as f:
    img = f.read()
  return remove(img)

def evolve_image(original_img: bytes, feed: Feed) -> bytes:
  # 仮の処理
  if (feed.name == "チョウチンアンコウ"):
    fish_path = "./static/fish2.png"
  elif (feed.name == "カクレクマノミ"):
    fish_path = "./static/fish3.png"
  elif (feed.name == "ホオジロザメ"):
    fish_path = "./static/fish4.png"
  else:
    fish_path = ""
  if fish_path != "":
    with open(fish_path, "rb") as f:
      fish_data = f.read()
  else:
    fish_data = original_img
  return fish_data

def load_fish_image(path: str) -> bytes:
  if not os.path.exists(path):
    raise FileNotFoundError("Fish not found")
  
  with open(path, "rb") as f:
    return f.read() 
    
def save_fish_image(img_bytes: bytes, path: str):
  with open(path, "wb") as f:
    f.write(img_bytes)
  return path