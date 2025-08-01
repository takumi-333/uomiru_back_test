from flask import Blueprint, request, session, jsonify, send_file
from io import BytesIO
import os
from app.services.feed_service import get_all_feeds, get_feed_img_by_path

feed_bp = Blueprint("feed", __name__, url_prefix="/feeds")

@feed_bp.route("", methods=["GET"])
def get_feeds():
  feeds = get_all_feeds()
  return jsonify(feeds), 200

@feed_bp.route("/image", methods=["GET"])
def get_feed_image():
  path = request.args.get("path")
  if not path:
    return jsonify({"error": "pathが必要です"}), 400

  image_data = get_feed_img_by_path(path)
  if not image_data:
    return jsonify({"error": "餌の画像が見つかりませんでした"}), 404

  return send_file(BytesIO(image_data), mimetype="image/png")