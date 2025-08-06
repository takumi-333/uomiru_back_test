from app.domain.repositories.feed_repository import IFeedRepository
from app.services.fish_manager import load_fish_image

class FeedUsecase:
  def __init__(self, repo: IFeedRepository):
    self.repo = repo

  def list_all_feeds(self):
    return [feed.to_dict() for feed in self.repo.get_all()]
  
  def get_image(self, path: str) -> bytes | None:
    return load_fish_image(path)