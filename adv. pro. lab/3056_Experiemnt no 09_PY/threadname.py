from threading import *
def new():
    for x in range(6):
        print("hello world...",current_thread().getName())
t1=Thread(target=new)
print(current_thread().getName)
t1.start()
t1.join()
print("bye",current_thread().getName())
