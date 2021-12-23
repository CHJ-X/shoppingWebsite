from flask import Blueprint

user = Blueprint('user', __name__)

@user.route('/user/hello')
def hello():
  return '/user/hello'