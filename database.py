# %%
from flask_sqlalchemy import SQLAlchemy

# %%
db = SQLAlchemy()

class User(db.Model):
  __tablename = 'user'
  __table_args__ = {'mysql_collate':'utf8_general_cli'}

  _id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True)
  password = db.Column(db.String(20))
  mail = db.Column(db.String(30))
  address = db.Column(db.String(100))
  gender = db.Column(db.String(5))


class Admin(db.Model):
  username = db.Column(db.String(20), unique=True)
  password = db.Column(db.String(20))