class Fish:
  def __init__(self, img_path: str, size: int, user_id: str, id: int | None=None):
    self.id = id
    self.img_path = img_path
    self.size = size
    self.user_id = user_id