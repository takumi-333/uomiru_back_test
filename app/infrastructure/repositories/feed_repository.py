import os, json
from typing import List
from app.domain.entities.feed import Feed
from app.domain.repositories.feed_repository import IFeedRepository

class FeedRepository(IFeedRepository):
  FEED_DIR = "./mock_db/feeds"

  def get_all(self) -> List[Feed]:
    feeds = []
    for filename in os.listdir(self.FEED_DIR):
      if filename.endswith(".json"):
        with open(os.path.join(self.FEED_DIR, filename), "r", encoding="utf-8") as f:
          data = json.load(f)
          feed = Feed(
            id=data.get("id", ""),
            name=data.get("name", ""),
            feature=data.get("feature", ""),
            img_path=data.get("img_path", "")
          )
          feeds.append(feed)
    return feeds
  
  def get_image_by_path(self, path: str) -> bytes | None:
    if not os.path.exists(path):
      return None
    with open(path, "rb") as f:
      return f.read()