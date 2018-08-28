# from threading import Thread
# import time
#
# def sing():
# 	for i in range(10):
# 		print("singing")
# 		time.sleep(1)
#
# def dance():
# 	for i in range(10):
# 		print("dancing")
# 		time.sleep(1)
#
# t1 = Thread(target = sing)
# t2 = Thread(target = dance)
l=[1,2,34,5,54,6,7]
for i in range(len(l)):
	for k in range(len(l)):
		if l[i]>l[k]:
			l[i],l[k]=l[k],l[i]
	print(l)


