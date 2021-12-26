from flask import Blueprint,session

admin = Blueprint('admin', __name__)

#商品添加接口
@admin.route("/admin/goodsAdd",methods=["POST"])
def goodsAdd():
	if request.method == "POST":

		form = request.form
		image = request.files["image"]
		save_path = "./static/goods/"+getOrderNum()+image.filename
		image.save(save_path)
		data  = {
			"name":form["name"],
			"price":form["price"],
			"image":save_path
		}
		goods = Goods(**data)
		db.session.add(goods)
		db.session.commit()
		return result(200)

#获取所有商品信息
@admin.route("/admin/checkGoods",methods=["POST","GET"])
def checkGoods():
	if request.method == "GET":

		nums = Goods.query.count()
		return result(200,{"nums":nums})

	if request.method == "POST":
		start = request.form["start"]
		nums = request.form["nums"]
		goods = Goods.query.offset(start).limit(nums)
		data = dict()
		data["data"] = []
		for good in goods:
			dic = good.__dict__
			del dic["_sa_instance_state"]
			data["data"].append(dic)
		return result(200,data)


#商品的删除
@admin.route("/admin/goodsDelete",methods=["DELETE"])
def goodsDelete():
	if request.method=="DELETE":

		_id = request.form["id"]
		Goods.query.filter_by(_id=_id).delete()
		return result(200)

#添加管理员
@admin.route("/admin/add",methods=["POST"])
def adminAdd():
	if request.method == "POST":

		form = request.form
		data = {
			"username":form["username"],
			"password":md5(form["password"])
		}
		admin = Admin(**data)
		db.session.add(admin)
		db.session.commit()
		return result(200)


#查看所有人商品订单订单情况
@admin.route("/admin/receipt/<int:start>/<int:nums>",methods=["POST","GET"])
def adminReceipt(start,nums):
	if request.method == "GET":

		nums = Receipt.query.all().count()
		return result(200,{"nums":nums})

	if request.method == "POST":

		receipts = Receipt.query.offset(start).limit(nums)
		data = dict()
		data["data"] = []
		for receipt in receipts:
			goodsIdList = receipt.get_goods_id_list()
			dic = receipt.__dict__
			del dic["_sa_instance_state"]
			dic["goodsList"] = []
			for goodsId in goodsIdList:
				goods = Goods.query.with_entities(Goods.name,Goods.price).filter_by(_id=goodsId)
				d = goods.__dict__
				del d["_sa_instance_state"]
				dic["goodsList"].append(d)
			data["data"].append(dic)
		return result(200,data)

#获得所有用户信息
@admin.route("/admin/getUsers",methods=["POST","GET"])
def getUsers():
	if request.method == "GET":

		nums = User.query.count()
		return result(200,{"nums":nums})

	if request.method == "POST":
		start = request.form["start"]
		nums = request.form["nums"]
		users = User.query.offset(start).limit(nums)
		data = dict()
		data["data"] = []
		for user in users:
			dic = user.__dict__
			del dic["_sa_instance_state"]
			
			
			data["data"].append(dic)
		return result(200,data)
