import hashlib
import hmac
md5 = hashlib.md5()
md5.update('我的密码  123456?'.encode('utf-8'))
print('md5加密结果：',md5.hexdigest())

sha = hashlib.sha1()
sha.update('789456'.encode('utf-8'))
print('sha加密结果：',sha.hexdigest())


# hmac

msg = b'Hello, world!'
# message = b'Hello, world!'
key = b'123'
res = hmac.new(key, msg, hashlib.md5)
print('hmac加密结果：',res.hexdigest())
