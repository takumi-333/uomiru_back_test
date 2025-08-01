from flask import Blueprint, request, session, jsonify, send_file
from io import BytesIO
import json
from app.services.feed_service import get_all_feeds

feed_bp = Blueprint("feed", __name__, url_prefix="/feeds")

@feed_bp.route("", methods=["GET"])
def get_feeds():
  feeds = get_all_feeds()
  return jsonify(feeds), 200

