#coding=utf-8

from multiprocessing import Pool,Manager
import time

def writer(q):
	for i in "laowang":
		q.put(i)
		print("")
		time.sleep(1)

def reader(q):
	while True:
		if not q.empty():
			msg = q.get()
			print(msg)
			if msg == "g":
				break	
			time.sleep(1)

p = Pool(3)
q = Manager().Queue()#创建一个无限大小的队列
p.apply_async(writer,(q,))
p.apply_async(reader,(q,))
p.join()


p.close()