from app.models.user_model import create_user_file, delete_user_file, verify_login, load_user

def create_user(user_id, password):
  return create_user_file(user_id, password)

def delete_user(user_id):
  return delete_user_file(user_id)

def login_user(user_id, password):
  return verify_login(user_id, password)

def get_user_by_id(user_id):
  return load_user(user_id)
