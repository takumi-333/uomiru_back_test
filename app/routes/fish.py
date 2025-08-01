from flask import Blueprint, request, session, jsonify, send_file
from io import BytesIO
import json
from app.services.fish_service import generate_fish_image, evolve_fish_image, get_fish_by_path

fish_bp = Blueprint("fish", __name__, url_prefix="/fish")

@fish_bp.route("/generate", methods=["POST"])
def generate():
  user_id = session.get("user_id")
  if not user_id:
    return jsonify({"error": "ログインが必要です"}), 401

  data = request.json
  ans = data.get("ans")
  if not ans:
    return jsonify({"error": "ansが必要です"}), 400

  output_data = generate_fish_image(user_id, ans)
  output_io = BytesIO(output_data)
  output_io.seek(0)
  return send_file(output_io, mimetype='image/png'), 201

@fish_bp.route("/evolve", methods=["POST"])
def evolve():
  user_id = session.get("user_id")
  if not user_id:
    return jsonify({"error": "ログインが必要です"}), 401
  
  feed_id = request.form.get("feed_id")
  if not feed_id:
    return jsonify({"error": "feed_idが必要です"}), 400
  
  result_img = evolve_fish_image(user_id, feed_id)
  output_io = BytesIO(result_img)
  output_io.seek(0)
  return send_file(output_io, mimetype='image/png'), 201

@fish_bp.route("", methods=["GET"])
def get_fish():
  path = request.args.get("path")
  if not path:
    return jsonify({"error": "pathが必要です"}), 400

  image_data = get_fish_by_path(path)
  if not image_data:
    return "", 204

  return send_file(BytesIO(image_data), mimetype="image/png")
