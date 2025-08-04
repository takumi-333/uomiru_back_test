from app.domain.repositories.feed_repository import IFeedRepository

class FeedUsecase:
  def __init__(self, repo: IFeedRepository):
    self.repo = repo

  def list_all_feeds(self):
    return [feed.to_dict() for feed in self.repo.get_all()]
  
  def get_image(self, path: str) -> bytes | None:
    return self.repo.get_image_by_path(path)