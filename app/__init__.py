from flask import Flask
from flask_cors import CORS
from app.infrastructure.db.base import db
import os

def create_app():
  app = Flask(__name__)
   # 本番では環境変数で設定
  app.secret_key = "dev-secret"

  app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://{user}:{password}@{host}:{port}/{dbName}".format(
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    host = os.getenv('DB_HOST', 'localhost'),
    port = os.getenv('DB_PORT'),
    dbName = os.getenv('DB_NAME')
  )
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

  db.init_app(app)

  CORS(app, supports_credentials=True)

  # Blueprint登録
  from .routes.feed_route import feed_bp
  from .routes.fish_route import fish_bp
  from .routes.user_route import user_bp

  app.register_blueprint(fish_bp)
  app.register_blueprint(user_bp)
  app.register_blueprint(feed_bp)

  with app.app_context():
    db.create_all()
  return app
