#import hashlib

import simplejson as json

from werkzeug.security import generate_password_hash, check_password_hash
def encrypt(pwd):
    return generate_password_hash(pwd)

def checkPwd(pwd, hashedPwd):
    return check_password_hash(hashedPwd,pwd)

# def md5(m):
# 	return hashlib.md5(m.encode()).hexdigest()

def result(code=200,d={}):
	data = dict()
	data['code'] = code 
	data['data'] = d
	return json.dumps(data,ensure_ascii=False)
