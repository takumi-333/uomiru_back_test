import os, json, bcrypt
from app.domain.entities.user import User
from app.domain.repositories.user_repository import IUserRepository

USER_DIR = "./mock_db/users"

class UserRepository(IUserRepository):
  def _get_path(self, user_id):
    return os.path.join(USER_DIR, f"{user_id}.json")
  
  def create(self, user: User) -> bool:
    path = self._get_path(user.id)
    if os.path.exists(path):
      return False
    with open(path, "w") as f:
      json.dump({
        "id": user.id,
        "hashed_pass": user.hashed_pass,
        "my_fish_path": user.my_fish_path
      }, f)
    return True
  
  def delete(self, user_id: str) -> bool:
    path = self._get_path(user_id)
    if os.path.exists(path):
      os.remove(path)
      return True
    return False
  
  def find_by_id(self, user_id: str) -> User | None:
    path = self._get_path(user_id)
    if not os.path.exists(path):
      return None
    with open(path) as f:
      data = json.load(f)
    return User(data["id"], data["hashed_pass"], data.get("my_fish_path", ""))
  
  def verify_password(self, user_id: str, password: str) -> bool:
    user = self.find_by_id(user_id)
    if not user:
      return False
    return bcrypt.checkpw(password.encode(), user.hashed_pass.encode())
  
  def save_fish_path(self, user_id: str, path: str):
    user = self.find_by_id(user_id)
    if not user:
      return
    user.my_fish_path = path
    self.create(user)