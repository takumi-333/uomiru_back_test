class Feed:
  def __init__(self, id: str, name: str, feature: str, img_path: str, prompt_info: str=""):
    self.id = id
    self.name = name
    self.feature = feature
    self.prompt_info = prompt_info
    self.img_path = img_path

  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "feature": self.feature,
      "prompt_info": self.prompt_info,
      "img_path": self.img_path,
    }