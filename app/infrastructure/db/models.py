from app.infrastructure.db.base import db

class UserModel(db.Model):
  __tablename__ = "users"
  id = db.Column(db.String(50), primary_key=True)
  hashed_pass = db.Column(db.String(128), nullable=False)

  fish = db.relationship(
    "FishModel",
    back_populates="user",
    uselist=False,
    cascade="all, delete-orphan"
  )
  
class FishModel(db.Model):
  __tablename__ = "fish"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  size = db.Column(db.Integer, nullable=False)
  img_path = db.Column(db.String(256), nullable=False)
  user_id = db.Column(db.String(50), db.ForeignKey("users.id"), unique=True)

  user = db.relationship(
    "UserModel",
    back_populates="fish"
  )

class FeedModel(db.Model):
  __tablename__ = "feeds"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(50), nullable=False)
  img_path = db.Column(db.String(256), nullable=False)
  features = db.Column(db.Text, nullable=True)
  prompt_info = db.Column(db.Text, nullable=True)
  size = db.Column(db.Integer, nullable=False)