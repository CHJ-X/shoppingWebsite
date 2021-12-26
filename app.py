from flask import Flask,request,session
from database import *
from config import *
from user import user
from admin import admin
from utils import *
import traceback

app = Flask(__name__, static_folder="static")
app.config.from_object(MySQLConfig)

with app.app_context():
  db.init_app(app)
  db.create_all()

app.register_blueprint(admin)
app.register_blueprint(user)

#拦截登陆前操作
@app.before_request
def before():
	try:
		data = json.loads(request.get_data(as_text=True))
		request.form = data
	except:
		pass
	url = request.path #当前请求的URL
	passUrl = WHITE_NAME_LIST
	if url in passUrl:
		pass 
	elif "static" in url:
		pass
	elif "/goods/detail/" in url:
		pass 
	else:
		_id = session.get("_id",None)
		if not _id:
			return result(203,{"info":"未登录"})
		else:
			pass 


@app.route('/log')
def log():
  
  return '/'

#用户登录
@app.route('/login', methods=['POST', 'GET'])
def login():
  if request.method == "POST":
    username = request.form['username']
    password = request.form['password']
    #password = md5(password)
    admin = Admin.query.filter_by(username=username).first()
    if admin:
      if checkPwd(password, admin.password):
      #if admin.password == password:
        session["_id"] = admin._id
        db.session.commit()
        return result(201,{"info":"管理员登录成功"})
      else:
        return result(400,{"info":"密码不正确"})
    else:
      user = User.query.filter_by(username=username).first()
      if user:
        if checkPwd(password, user.password):
        #if user.password == password:
          session["_id"] = user._id
          db.session.commit()
          return result(200,{"info":"用户登录成功"})
        else:
          return result(400,{"info":"密码不正确"})
      else:
        return result(401,{"info":"无该用户信息"})
  if request.method == "GET":
    return result()

@app.route("/quit",methods=["POST"])
def quit():
	_id = session["_id"]
	del session["_id"]
	return result(200)

#用户注册
@app.route("/register",methods=["POST"])
def register():
  if request.method=="POST":
    try:
      username = request.form["username"]
      password = request.form["password"]
      mail = request.form["mail"]
      address = request.form["address"]
      password = encrypt(password)
      user = User(username=username,password=password,mail=mail,address=address)
      
      try:
        db.session.add(user)
        db.session.commit()
      except:
        return result(400,{"info":"重复注册"})
      user = User.query.filter_by(username=username).first()
      court = Court(user_id=user._id)
      db.session.add(court)
      db.session.commit()
      session["_id"] = user._id
      return result(200)
    except:
      return result(502,{"info":"服务端出错"})

@app.route("/goods/detail/<int:goodsId>")
def goods_detail(goodsId):
	if request.method=="GET":
		goods = Goods.query.get(goodsId)
		data= goods.__dict__
		del data["_sa_instance_state"]
		return result(200,data)



if (__name__ == "__main__"):
  app.run()
