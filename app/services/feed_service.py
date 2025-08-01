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