from flask import Blueprint
from app.controllers.feed_controller import get_feeds_controller, get_feed_image_controller

feed_bp = Blueprint("feed", __name__, url_prefix="/feeds")

feed_bp.route("", methods=["GET"])(get_feeds_controller)
feed_bp.route("/image", methods=["GET"])(get_feed_image_controller)
