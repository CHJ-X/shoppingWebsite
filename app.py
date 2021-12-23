from flask import Flask, session, request
from database import*
from config import*
#blueprint
from user import user
from admin import admin


app = Flask(__name__, static_folder="static")
app.config.from_object(MySQLConfig)

with app.app_context():
  db.init_app(app)
  db.create_all()

app.register_blueprint(admin)
app.register_blueprint(user)

@app.route('/')
def index():
  return '/'


@app.route('/login', method=['POST'])
def login():
  return None

@app.route('/register')
def register():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']


if (__name__ == "__main__"):
  app.run()
