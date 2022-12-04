# 3_A - odd even prime
#program to identify inputed no is odd or even
x =int(input("enter a no:"))
if x%2==0:
    print(x," is even!!")
else:
    print(x," is odd!!")

#program to identify given no is prime or not
x1 =int(input("enter a no:"))
for y in range(2,x1):
    if x1%y==0:
            print(x1," is not prime")
            break
else:
    print(x1," is prime")
