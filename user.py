from flask import Blueprint,session

user = Blueprint('user', __name__)


#购买商品生成订单
@user.route("/user/buyGoods",methods=["POST"])
def buyGoods():
	if request.method == "POST":
		sId = session.get("_id",None)
		form = request.form
		user = User.query.get(sId)
		goodsList = request.form["goodsList"]
		itemIdList = [] 
		itemCount = ReceiptItem.query.count()
		#购物车清空
		court = Court.query.filter_by(user_id=sId).first()
		try:
			for goods in goodsList:
				item = ReceiptItem(goodsId=goods["id"],number=goods["number"])
				db.session.add(item)
				goods = Goods.query.get(goods["id"])
				court.goods.remove(goods)
				itemCount = itemCount + 1
				itemIdList.append(itemCount)
			data = {
				"orderNum":getOrderNum(),
				"payValue":form["payValue"],
				"cutoffValue":form["cutoffValue"],
				"user_id":sId,
				"itemId":str(itemIdList)
			}
			receipt = Receipt(**data)
			db.session.add(receipt)
			db.session.commit()
			return result(200)
		except:
			traceback.print_exc()
			return result(502,{"info":"服务端错误"})

#查看个人商品订单情况
@user.route("/user/checkReceipt")
def checkReceipt():
	if request.method == "GET":
		sId = session['_id']
		receipts = Receipt.query.filter_by(user_id=sId)
		data = dict()
		data["data"] = []
		try:
			for receipt in receipts:
				goodsIdList = receipt.get_goods_id_list()
				dic = receipt.__dict__
				del dic["_sa_instance_state"]
				dic["goodsList"] = []
				for goodsId in goodsIdList:
					goods = Goods.query.get(goodsId)
					d = {
						"name":goods.name,
						"price":goods.price
					}
					print("="*30)
					print(d)
					print("="*30)
					dic["goodsList"].append(d)
				data["data"].append(dic)
			return result(200,data)
		except:
			traceback.print_exc()
			return result(502,{"info":"服务端错误"})

#获取自己购物车和商品信息
@user.route("/user/checkCourt")
def checkCourt():
	if request.method == "GET":
		sId = session.get("_id")
		court = Court.query.filter_by(user_id=sId).first()
		if court.number == 0:
			return result(200,{"goods":[]})
		goods = court.goods.all()
		data = dict()
		data["data"] = []
		for good in goods:
			dic = good.__dict__
			data["data"].append({
				"_id":good._id,
				"name":good.name,
				"price":good.price,
				"image":good.image
				})

		return result(200,data)

#添加商品到购物车
@user.route("/user/add2Court",methods=["POST"])
def add2Court():
	if request.method == "POST":
		goodsId = request.form["goodsId"]
		sId = session["_id"]
		court = Court.query.filter_by(user_id=sId).first()
		goods = Goods.query.get(goodsId)
		court.goods.append(goods)
		db.session.commit()
		return result(200)

#移除购物车商品信息
@user.route("/user/rmFromCourt",methods=["POST"])
def rmFromCourt():
	if request.method == "POST":
		goodsId = request.form["goodsId"]
		sId = session["_id"]
		court = Court.query.filter_by(user_id=sId).first()
		goods = Goods.query.get(goodsId)
		court.goods.remove(goods)
		db.session.commit()
		return result()

#查看用户个人信息
@user.route("/user/info",methods=["GET"])
def userInfo():
	sId = session['_id'] 
	user = User.query.get(sId)
	user = user.__dict__
	del user["_sa_instance_state"]
	del	user['password']
	return result(200,user)

