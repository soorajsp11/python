from threading import *
# def new():
#     for x in range(7):
#         print("hello world!...")
# t1 = Thread(target=new)
# t1.start()
# print("bye")
# #run and see output
# print("\n")
#now 
from threading import *
def new():
    for x in range(7):
        print("hello world!...")
t1 = Thread(target=new)
t1.start()
t1.join()
print("bye")