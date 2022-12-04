from threading import *
class A(Thread):
    def run(self):
        for x in range(7):
            print("child =",current_thread().getName())
obj=A()
obj.start()
obj.join()
print("control return to",current_thread().getName())
