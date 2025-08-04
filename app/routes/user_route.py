from flask import Blueprint
from app.controllers.user_controller import (
  register_controller, delete_controller,
  login_controller, logout_controller,
  check_auth_controller, get_current_user_controller
)

user_bp = Blueprint("user", __name__)

user_bp.route("/users", methods=["POST"])(register_controller)
user_bp.route("/users/<user_id>", methods=["DELETE"])(delete_controller)
user_bp.route("/login", methods=["POST"])(login_controller)
user_bp.route("/auth/check", methods=["GET"])(check_auth_controller)
user_bp.route("/auth/user", methods=["GET"])(get_current_user_controller)
user_bp.route("/logout", methods=["POST"])(logout_controller)