from flask import Blueprint

user = Blueprint('admin', __name__)

@admin.route('/admin/hello')
def hello():
  return '/admin/hello'


@admin.route('/admin/hello')
def hello():
  return '/admin/hello'