from flask import Blueprint, request, jsonify
from app.services.user_service import create_user, delete_user

user_bp = Blueprint("user", __name__, url_prefix="/users")

@user_bp.route("", methods=["POST"])
def create():
  data = request.json
  user_id = data.get("user_id")
  password = data.get("password")
  if not user_id or not password:
    return jsonify({"error": "user_idとpasswordが必要です"}), 400

  success, message = create_user(user_id, password)
  if success:
    return jsonify({"message": message}), 201
  return jsonify({"error": message}), 400

@user_bp.route("/<user_id>", methods=["DELETE"])
def delete(user_id):
  success, message = delete_user(user_id)
  if success:
    return jsonify({"message": message}), 200
  return jsonify({"error": message}), 404
