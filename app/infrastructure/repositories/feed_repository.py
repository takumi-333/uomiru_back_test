from typing import List
from app.domain.entities.feed import Feed
from app.domain.repositories.feed_repository import IFeedRepository
from app.infrastructure.db.models import FeedModel

class FeedRepository(IFeedRepository):
  def get_all(self) -> List[Feed]:
    feed_models = FeedModel.query.all()
    feeds = [
      Feed(
        id=feed_model.id,
        name=feed_model.name,
        feature=feed_model.features,
        img_path=feed_model.img_path,
        prompt_info=feed_model.prompt_info,
        size=feed_model.size,
      )
      for feed_model in feed_models
    ]
    return feeds
  
  def find_by_id(self, id: int):
    model = FeedModel.query.filter_by(id=id).first()
    if not model:
      return None
    return Feed(
      id=model.id,
      name=model.name,
      feature=model.features,
      img_path=model.img_path,
      prompt_info=model.prompt_info,
      size=model.size
    )