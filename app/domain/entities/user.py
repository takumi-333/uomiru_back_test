class User:
  def __init__(self, user_id: str, hashed_pass: str):
    self.id = user_id
    self.hashed_pass = hashed_pass
  
  def to_res_dict(self):
    return {
      "id": self.id
    }