#1- function with 2 arguments
def myself(name,sirname):
    print(name,"",sirname)
myself("Suraj", "Patil")

#2- functions with 3 arguments
def volume(length, breadth, height):
    volume = length*breadth*height
    print("volume is =",volume,"unit")
volume(10, 5, 15)

def interest(amount,rate,time):
    interest=(amount*rate*time)/100;
    print("interest=",interest)
interest(100,13,2)

#3- function with multiple arguments
def addition(x,y):
    print("addition is:",x+y)
addition(10,20)

#user input
def addition():
    x=int(input('enter first number:'))
    y=int(input('enter second number:'))
    print("addition is:",x+y)
addition()

#average
def average(m1,m2,m3,m4,m5):
    sum=m1+m2+m3+m4+m5
    avg=sum/5
    print('sum=',sum,'average=',avg)
average(10,20,30,40,50)

