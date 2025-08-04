from flask import request, session, jsonify
from app.usecase.user_usecase import UserUsecase
from app.infrastructure.repositories.user_repository import UserRepository

user_usecase = UserUsecase(UserRepository())

def register_controller():
  data = request.json
  user_id, password = data.get("user_id"), data.get("password")
  if not user_id or not password:
    return jsonify({"error": "user_idとpasswordが必要です"}), 400
  
  if user_usecase.register(user_id, password):
    return jsonify({"message": "ユーザ登録成功"}), 201
  return jsonify({"error": "ユーザがすでに存在します"}), 400

def delete_controller(user_id):
  if user_usecase.delete_user(user_id):
    return jsonify({"message": "ユーザ削除成功"}), 200
  return jsonify({"error": "ユーザが存在しません"}), 404

def login_controller():
  data = request.json
  user_id, password = data.get("user_id"), data.get("password")
  if not user_id or not password:
    return jsonify({"error": "user_idとpasswordが必要です"}), 400
  if user_usecase.login(user_id, password):
    print("session 更新")
    session["user_id"] = user_id
    return jsonify({"message": "認証成功"}), 200
  return jsonify({"error": "認証失敗"}), 401

def check_auth_controller():
  user_id = session.get("user_id")
  return jsonify({
    "logged_in": bool(user_id),
    "user_id": user_id
  }), 200

def get_current_user_controller():
  user_id = session.get("user_id")
  if not user_id:
    return jsonify({"error": "ログインしていません"}), 401
  user = user_usecase.get_user(user_id)
  if user:
    return jsonify(user), 200
  return jsonify({"error": "ユーザが見つかりませんでした"}), 404

def logout_controller():
  session.clear()
  return jsonify({"message": "ログアウトしました"}), 200