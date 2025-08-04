import bcrypt
from app.domain.entities.user import User
from app.domain.repositories.user_repository import IUserRepository

class UserUsecase:
  def __init__(self, repo: IUserRepository):
    self.repo = repo

  def register(self, user_id: str, password: str) -> bool:
    hashed_pass = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    user = User(user_id, hashed_pass)
    return self.repo.create(user)
  
  def delete_user(self, user_id: str) -> bool:
    return self.repo.delete(user_id)
  
  def login(self, user_id: str, password: str) -> bool:
    return self.repo.verify_password(user_id, password)
  
  def get_user(self, user_id: str) -> dict | None:
    user = self.repo.find_by_id(user_id)
    if user:
      return {
        "user_id": user.user_id,
        "my_fish_path": user.my_fish_path
      }
    return None