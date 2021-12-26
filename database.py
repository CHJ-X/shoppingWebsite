from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename = 'user'
  __table_args__ = {'mysql_collate':'utf8_general_ci'}

  _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(20), unique=True)
  password = db.Column(db.String(256))
  mail = db.Column(db.String(30))
  address = db.Column(db.String(100))


class Admin(db.Model):
  __tablename = 'admin'
  __table_args__ = {'mysql_collate':'utf8_general_ci'}
  _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(20), unique=True)
  password = db.Column(db.String(256))

goodsCourt = db.Table("goodsCourt",
	db.Column("goods_id",db.Integer,db.ForeignKey("goods._id")),
	db.Column("court_id",db.Integer,db.ForeignKey("court._id"))
	)

#购物车
class Court(db.Model):
  __tablename = 'court'
  __table_args__ = {'mysql_collate':'utf8_general_ci'}
  _id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
  user_id = db.Column(db.Integer)#外键
  number = db.Column(db.Integer,default=0)
  goods = db.relationship("Goods",secondary=goodsCourt,backref=db.backref("court",lazy="dynamic"),lazy="dynamic")
#商品
class Goods(db.Model):
  __tablename = 'goods'
  __table_args__ = {'mysql_collate':'utf8_general_ci'}
  _id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
  name = db.Column(db.String(100))
  price = db.Column(db.Float(20))
  image = db.Column(db.String(256))


class Receipt(db.Model):
	__tablename__ = "receipt"
	__table_args__ = {'mysql_collate':'utf8_general_ci'}
	_id = db.Column(db.Integer,primary_key=True, autoincrement=True, nullable=False)
	orderNum = db.Column(db.String(30))
	payValue = db.Column(db.Float(10))
	user_id = db.Column(db.Integer,db.ForeignKey("user._id"))
	itemId = db.Column(db.String(100),default="[]")

	def get_goods_id_list(self):
		idStrList = self.itemId[1:-1].split(',')
		idList = []
		for item in idStrList:
			idList.append(int(item))
		return idList

class ReceiptItem(db.Model):

	__tablename__ = "receipt_item"
	__table_args__ = {'mysql_collate':'utf8_general_ci'}
	_id = db.Column(db.Integer,primary_key=True, autoincrement=True, nullable=False)
	goodsId = db.Column(db.Integer)
	number = db.Column(db.Integer,default=0)
