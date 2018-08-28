from threading import Thread,Lock
import time
num = 0

def work1():
	global num
	m.acquire(True)
	for i in range(10000):
		num+=1
	m.release()
	print(num)
	      
def work2():
	global num
	m.acquire(True)
	for i in range(10000):
		num+=1
	m.release()
	print(num)
	m.clock()
t1 = Thread(target=work1)
t1.start()
#t1.join()

t2 = Thread(threading=work2)
t2.start()