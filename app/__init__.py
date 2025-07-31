from flask import Flask
from flask_cors import CORS

def create_app():
  app = Flask(__name__)
   # 本番では環境変数で設定
  app.secret_key = "dev-secret"

  CORS(app, supports_credentials=True)

  # Blueprint登録
  from .routes.auth import auth_bp
  from .routes.fish import fish_bp
  from .routes.user import user_bp

  app.register_blueprint(auth_bp)
  app.register_blueprint(fish_bp)
  app.register_blueprint(user_bp)

  return app
