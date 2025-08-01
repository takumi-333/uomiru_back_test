from rembg import remove
import os
import json

def get_all_feeds():
  FEED_DIR = './mock_db/feeds'
  feeds = []
  for filename in os.listdir(FEED_DIR):
    if filename.endswith('.json'):
      with open(os.path.join(FEED_DIR, filename), 'r', encoding='utf-8') as f:
        feed_data = json.load(f)
        feeds.append(feed_data)
  
  return feeds

def get_feed_img_by_path(path):
  if not os.path.exists(path):
    return None
  with open(path, "rb") as f:
    return f.read()
  