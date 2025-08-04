from flask import Blueprint
from app.controllers.fish_controller import generate_fish_controller, evolve_fish_controller, get_fish_controller

fish_bp = Blueprint("fish", __name__, url_prefix="/fish")

fish_bp.route("/generate", methods=["POST"])(generate_fish_controller)
fish_bp.route("/evolve", methods=["POST"])(evolve_fish_controller)
fish_bp.route("", methods=["GET"])(get_fish_controller)