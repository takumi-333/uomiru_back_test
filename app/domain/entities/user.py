class User:
  def __init__(self, user_id: str, hashed_pass: str, my_fish_path: str = ""):
    self.id = user_id
    self.hashed_pass = hashed_pass
    self.my_fish_path = my_fish_path