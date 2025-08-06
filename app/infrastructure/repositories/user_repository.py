import bcrypt
from app.domain.entities.user import User
from app.domain.repositories.user_repository import IUserRepository
from app.infrastructure.db.models import UserModel
from app.infrastructure.db.base import db

class UserRepository(IUserRepository):
  def create(self, user: User) -> bool:
    # すでにidが同じユーザが存在するか確認
    existing = UserModel.query.filter_by(id=user.id).first()
    if existing:
      return False
    
    model = UserModel(
      id=user.id,
      hashed_pass=user.hashed_pass,
    )
    db.session.add(model)
    db.session.commit()
    return True
  
  def delete(self, user_id: str) -> bool:
    model = UserModel.query.filter_by(id=user_id).first()
    if not model:
      return False
    db.session.delete(model)
    db.session.commit()
    return True
  
  def find_by_id(self, user_id: str) -> User | None:
    model = UserModel.query.filter_by(id=user_id).first()
    if not model:
      return None
    return User(
      user_id=model.id,
      hashed_pass=model.hashed_pass,
    )
  
  def verify_password(self, user_id: str, password: str) -> bool:
    model = UserModel.query.filter_by(id=user_id).first()
    if not model:
      return False
    return bcrypt.checkpw(password.encode(), model.hashed_pass.encode())
  