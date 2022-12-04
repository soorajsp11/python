#without multithreading
import time
def d2(n):
    for x in n:
        time.sleep(1)
        print(x%2)
def d3(n):
    for x in n:
        time.sleep(1)
        print(x%3)
n=[2, 4, 3, 6, 7]
s=time.time()
d2(n)
d3(n)
e=time.time()
print(e-s)


#with multithreading
from threading import *
print("\n")
def d(n):
    for x in n:
        time.sleep(1)
        print(x%2)
def d1(n):
    for x in n:
        time.sleep(1)
        print(x%3)
n=[2, 4, 3, 6, 7]
s=time.time()
t1 = Thread(target=d, args=(n,))
t2 = Thread(target=d1, args=(n,))
t1.start()
t2.start()
t1.join()
t2.join()
e=time.time()
print(e-s)
