class Feed:
  def __init__(self, id: str, name: str, feature: str, img_path: str):
    self.id = id
    self.name = name
    self.feature = feature
    self.img_path = img_path

  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "feature": self.feature,
      "img_path": self.img_path,
    }