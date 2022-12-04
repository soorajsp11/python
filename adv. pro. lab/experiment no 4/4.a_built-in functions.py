# some buitl in functions in python

#1- absolute function 
x = abs(-8.35)
print(x);

# 2- binary function
x = bin(56)
print("binary value of 56 is:",x);

# 3- boolean function
# returns always True unless value is [],{},none or 0 etc
x = bool(1200)
print(x);

# 4 - char function 
x = chr(97)
print("chharacter value of 97 is:",x);

#5 - complex function (returns a complex number)
x = complex(2, 3)
print("complex number is:",x);

#6 - delete attribute function
class Student:
    name = "suraj"
    age = 21
    department = "CSE"
# delattr(Student, 'age')
print('name:',Student.name)
print('department:',Student.department)
print('age:',Student.age)

# 7 - dictionary function
x = dict(name="Suraj", lastname="Patil", dept="CSE", div="A")
print(x)

# 8 - divmod() // returns quotient and reminder while performing division operation
x = divmod(13, 2)
print("Quoteint & Reminder=",x);

# 9 - evaluate function
x = 'print(55)'
eval(x);
# 10 - exec() //same working as eval

# 11 - float() // returns a floting point number
x = float(96)
print("floating value of 96 is =",x);

# 12- id() // returns id of an object i.e. memory address
x = ('apple', 'banana', 'mango')
y = id(x)
print(y);

#13- input()
print("Enter your name:")
x = input()
print("hello, ",x)

#14- int()//returns integer number
x = int(3.35)
print("integer value of 3.35 is =",x)

#15- len()//returns length of object
mylist = ["apple", "banana", "mango"]
x = len(mylist)
print(x)

#16- max() // returns largest item
x = max(10, 15, 13);
print("largest number is:",x)

#17- min()// returns lowest value item
x = min(13, 11, 17);
print("smaller number is:", x);

#18- range()
x = range(9)
for n in x:
    print(n)

#19- round()//rounds a number 
x = round(5.453892, 2)
print("rounding value upto 2 digit is:",x)

#20- soted()//returns a sorted list
list =("a", "d", "b", "c")
x = sorted(list)
print(x);

#21- sum()//returns sum
a = (3,4,5,6,7,8)
x = sum(a)
print("sum is =",x)

#22- type() // returns type of an variable or datatype
a = {5,10,15,20,25}
b = ["apple", "banana", "mango"]
c = 33
d = 56.24
print("data-type of a is:",type(a));
print("data-type of b is:",type(b));
print("data-type of c is:",type(c));
print("data-type of d is:",type(d));
