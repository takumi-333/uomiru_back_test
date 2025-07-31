import os
import json
import bcrypt

USER_DIR = './mock_db/users'

def add_user(user_id, password):
  path = os.path.join(USER_DIR, f"{user_id}.json")
  if os.path.exists(path):
    return False, "ユーザがすでに存在します"
  hashed_pass = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
  user_data = {
    "user_id": user_id,
    "hashed_pass": hashed_pass,
    "my_fish_path": "",
  }
  with open(path, "w") as f:
    json.dump(user_data, f)
  return True, "ユーザ登録成功"

# ユーザ削除
def delete_user(user_id):
    path = os.path.join(USER_DIR, f"{user_id}.json")
    if not os.path.exists(path):
        return False, "ユーザが存在しません"
    os.remove(path)
    return True, "ユーザ削除成功"

# ログイン認証
def login(user_id, password):
    path = os.path.join(USER_DIR, f"{user_id}.json")
    if not os.path.exists(path):
      return False
    with open(path, "r") as f:
      user_data = json.load(f)
    stored_hash = user_data["hashed_pass"].encode()
    return bcrypt.checkpw(password.encode(), stored_hash)


def update_user_fish_path(user_id, file_path):
  path = os.path.join(USER_DIR, f"{user_id}.json")
  if not os.path.exists(path):
    raise FileNotFoundError(f'ユーザが存在しません: {path}')
  
  with open(path, 'r', encoding='utf-8') as f:
    user_data = json.load(f)

  user_data['my_fish_path'] = file_path
  with open(path, "w") as f:
    json.dump(user_data, f)


def get_user(user_id):
  path = os.path.join("./mock_db/users", f"{user_id}.json")
  if not os.path.exists(path):
    return False, {}
  
  with open(path, "r", encoding="utf-8") as f:
    user_data = json.load(f)
  
  filtered_user_data = {
    "user_id": user_data.get("user_id"),
    "my_fish_path": user_data.get("my_fish_path"),
  }
  return True, filtered_user_data