from app.infrastructure.db.base import db

class UserModel(db.Model):
  __tablename__ = "users"
  id = db.Column(db.String(50), primary_key=True)
  hashed_pass = db.Column(db.String(128), nullable=False)
  my_fish_path = db.Column(db.String(256), nullable=True)

  