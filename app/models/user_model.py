import os
import json
import bcrypt

USER_DIR = "./mock_db/users"

def create_user_file(user_id, password):
  path = os.path.join(USER_DIR, f"{user_id}.json")
  if os.path.exists(path):
    return False, "ユーザがすでに存在します"
  hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
  data = {"user_id": user_id, "hashed_pass": hashed, "my_fish_path": ""}
  with open(path, "w") as f:
    json.dump(data, f)
  return True, "ユーザ登録成功"

def delete_user_file(user_id):
  path = os.path.join(USER_DIR, f"{user_id}.json")
  if not os.path.exists(path):
    return False, "ユーザが存在しません"
  os.remove(path)
  return True, "ユーザ削除成功"

def verify_login(user_id, password):
  path = os.path.join(USER_DIR, f"{user_id}.json")
  if not os.path.exists(path):
    return False
  with open(path, "r") as f:
    data = json.load(f)
  return bcrypt.checkpw(password.encode(), data["hashed_pass"].encode())

def save_user_fish_path(user_id, path):
  user_path = os.path.join(USER_DIR, f"{user_id}.json")
  with open(user_path, "r") as f:
    data = json.load(f)
  data["my_fish_path"] = path
  with open(user_path, "w") as f:
    json.dump(data, f)

def load_user(user_id):
  path = os.path.join(USER_DIR, f"{user_id}.json")
  if not os.path.exists(path):
    return None
  with open(path, "r") as f:
    data = json.load(f)
  return {
    "user_id": data["user_id"],
    "my_fish_path": data["my_fish_path"]
  }
