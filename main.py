from flask import Flask, request, send_file, jsonify, session, Response
from flask_cors import CORS
import os
from io import BytesIO
from fish_modules import genFish, evoFish, add_fish, get_fish
import json
from user import add_user, delete_user, login, update_user_fish_path, get_user

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret")
CORS(app, supports_credentials=True)

# 準備してあるfish.pngを背景透過してレスポンス
@app.route('/generate', methods=['POST'])
def generate_fish():
    data = request.json
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "ログインが必要です"}), 401
    
    ans = data.get("ans")
    if not ans:
        return jsonify({"error": "ansが必要です"}), 400
    
    new_fish = genFish(ans)

    file_path = add_fish(user_id, new_fish)
    update_user_fish_path(user_id, file_path)
    output_io = BytesIO(new_fish)
    output_io.seek(0)
    
    return send_file(output_io, mimetype='image/png'), 201

# 餌の画像と特徴データを受け取り、準備してあるfish2.pngを背景透過してレスポンス
@app.route('/evolve', methods=['POST'])
def evolve_fish():
    # 自分の魚の画像を取得
    if 'target_img' not in request.files:
      return jsonify({"error": "No target image file part"}), 400
    target_img = request.files['target_img']
    if target_img.filename== '':
      return jsonify({"error": "No selected file"}), 400
    
    # 餌の画像を取得
    if 'feed_img' not in request.files:
      return jsonify({"error": "No feed image file part"}), 400
    feed_img = request.files['feed_img']
    if feed_img.filename == '':
      return jsonify({"error": "No selected file"}), 400
    
    # 特徴データ(JSON形式)を取得
    json_data = request.form.get('feed_data')
    if not json_data:
      return jsonify({"error": "No JSON feed data part"}), 400
    try:
      feed_features = json.loads(json_data)
    except json.JSONDecodeError:
      return jsonify({"error": "Invalid JSON format"}), 400

    new_fish = evoFish(target_img, feed_img, feed_features)

    output_io = BytesIO(new_fish)
    output_io.seek(0)
    
    return send_file(output_io, mimetype='image/png'), 201

@app.route("/fish", methods=['GET'])
def get_your_fish():
  path = request.args.get("path")
  if not path:
    return Response("Path not provided", status=400)
  
  fish_img = get_fish(path)
  if fish_img is None:
    return Response(status=204)
  return Response(fish_img, mimetype="image/png")
  return

@app.route("/users", methods=["POST"])
def create_user():
  data = request.json
  if not data or "user_id" not in data or "password" not in data:
    return jsonify({"error": "user_idとpasswordが必要です"}), 400
  
  user_id = data["user_id"]
  password = data["password"]
  success, message = add_user(user_id, password)
  if success:
    return jsonify({"message": message}), 201
  else:
    return jsonify({"error": message}), 400

@app.route("/users/<user_id>", methods=["DELETE"])
def remove_user(user_id):
  success, message = delete_user(user_id)
  if success:
    return jsonify({"message": message}), 200
  else:
    return jsonify({"error": message}), 404

@app.route("/login", methods=["POST"])
def authenticate():
    data = request.json
    if not data or "user_id" not in data or "password" not in data:
      return jsonify({"error": "user_idとpasswordが必要です"}), 400

    user_id = data["user_id"]
    password = data["password"]

    success = login(user_id, password)
    if success:
      session["user_id"]= user_id
      return jsonify({"message": "認証成功"}), 200
    else:
      return jsonify({"error": "認証失敗"}), 401
    
@app.route("/auth/check", methods=['GET'])
def check_auth():
  if "user_id" in session:
    return jsonify({"logged_in": True, "user_id": session["user_id"]}), 200
  else:
    return jsonify({"logged_in": False}),  200
  
@app.route("/logout", methods=['POST'])
def logout():
  session.clear()
  return jsonify({"message":"ログアウトしました"}), 200

@app.route("/auth/user", methods=["GET"])
def get_current_user():
  user_id = session.get("user_id")
  if not user_id:
    return jsonify({"error": "ログインしていません"}), 401
  success, user_data = get_user(user_id)

  if success:
    return jsonify(user_data), 200
  else:
    return jsonify({"error": "ユーザが見つかりませんでした"}), 404

  
    
if __name__ == '__main__':
    app.run(debug=True)
