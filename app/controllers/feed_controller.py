from flask import request, jsonify, send_file
from io import BytesIO
from app.infrastructure.repositories.feed_repository import FeedRepository
from app.usecase.feed_usecase import FeedUsecase

feed_usecase = FeedUsecase(FeedRepository())

def get_feeds_controller():
  feeds = feed_usecase.list_all_feeds()
  return jsonify(feeds), 200

def get_feed_image_controller():
  path = request.args.get("path")
  if not path:
    return jsonify({"error": "pathが指定されていません"}), 400
  
  image_data = feed_usecase.get_image(path)
  if not image_data:
    return jsonify({"error": "餌の画像が見つかりませんでした"}), 404
  
  return send_file(BytesIO(image_data), mimetype="image/png"), 200