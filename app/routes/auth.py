from flask import Blueprint, request, session, jsonify, Response
from app.services.user_service import login_user, get_user_by_id

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
  data = request.json
  user_id = data.get("user_id")
  password = data.get("password")

  if not user_id or not password:
    return jsonify({"error": "user_idとpasswordが必要です"}), 400

  if login_user(user_id, password):
    session["user_id"] = user_id
    return jsonify({"message": "認証成功"}), 200
  return jsonify({"error": "認証失敗"}), 401

@auth_bp.route("/auth/check", methods=["GET"])
def check_auth():
  user_id = session.get("user_id")
  return jsonify({
    "logged_in": bool(user_id),
    "user_id": user_id
  }), 200

@auth_bp.route("/logout", methods=["POST"])
def logout():
  session.clear()
  return jsonify({"message": "ログアウトしました"}), 200

@auth_bp.route("/auth/user", methods=["GET"])
def get_current_user():
  user_id = session.get("user_id")
  if not user_id:
    return jsonify({"error": "ログインしていません"}), 401

  user_data = get_user_by_id(user_id)
  if user_data:
    return jsonify(user_data), 200
  return jsonify({"error": "ユーザが見つかりませんでした"}), 404
