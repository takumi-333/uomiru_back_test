from flask import request, session, jsonify, send_file
from io import BytesIO
from app.usecase.fish_usecase import FishUsecase
from app.infrastructure.repositories.fish_repository import FishRepository
from app.infrastructure.repositories.feed_repository import FeedRepository

fish_usecase = FishUsecase(FishRepository(), FeedRepository())

def generate_fish_controller():
  user_id = session.get("user_id")
  if not user_id:
    return jsonify({"error": "ログインが必要です"}), 401
  data = request.json
  ans = data.get("ans")
  if not ans:
    return jsonify({"error": "回答がありません"}), 400
  result = fish_usecase.generate_fish(user_id, ans)
  return send_file(BytesIO(result), mimetype="image/png"), 201

def evolve_fish_controller():
  user_id = session.get("user_id")
  if not user_id:
    return jsonify({"error": "ログインが必要です"}), 401
  id = request.form.get("id")
  if not id:
    return jsonify({"error": "餌が指定されていません"}), 400
  result = fish_usecase.evolve_fish(user_id, id)
  return send_file(BytesIO(result), mimetype="image/png"), 201

def get_fish_controller():
  user_id = session.get("user_id")
  if not user_id:
    return jsonify({"error": "ログインしていません"}), 401

  image_data = fish_usecase.get_fish_by_user_id(user_id)
  if not image_data:
    return "", 204

  return send_file(BytesIO(image_data), mimetype="image/png")