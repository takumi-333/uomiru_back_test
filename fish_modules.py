import os
from rembg import remove

IMAGE_FOLDER = os.path.join(os.getcwd(), 'static')
FISH_DB_DIR = './mock_db/fish'

# 魚の画像を生成し、bytes型で返す
def genFish(ans):
  print(ans)
  input_path = os.path.join(IMAGE_FOLDER, 'fish.png')
  with open(input_path, 'rb') as input_file:
      input_data = input_file.read()
  
  output_data = remove(input_data)
  return output_data

def evoFish(target_img, feed_img, feed_data):
  print(feed_data)
  input_path = os.path.join(IMAGE_FOLDER, 'fish2.png')
  with open(input_path, 'rb') as input_file:
    input_data = input_file.read()
  
  output_data = remove(input_data)
  return output_data


def add_fish(user_id, fish_img):
  file_path = os.path.join(FISH_DB_DIR, f'{user_id}.png')
  with open(file_path, 'wb') as f:
    f.write(fish_img)
  print(f'魚を保存しました: {user_id}.png')

  return file_path

def get_fish(path):
  if not os.path.exists(path):
    return None
  with open(path, "rb") as f:
    fish_img = f.read()
  return fish_img