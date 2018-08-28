import re
def tell():
	phone_ret = re.compile(r"^1[3-9]\d{9}$")
	while True:
		phone = input("输入手机号")
		ret = re.search(phone_ret,phone)
		if ret:
			print("正确的手机号")

		else:
			print("错误的手机号")
tell()
