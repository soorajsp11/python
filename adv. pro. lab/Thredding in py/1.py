import threading
def square(number):
    for i in number:
        print("square",i*i)
def cube(number):
    for i in number:
        print("cube",i*i*i)
arr=[1,2,3,4,5]
t1= threading.Thread(target=square,args=(arr,))
t2= threading.Thread(target=cube,args=(arr,))
t1.start()
t2.start()
t1.join()
t2.join()