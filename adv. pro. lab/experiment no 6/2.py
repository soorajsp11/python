class Person:
    def __init__(object, name, age): #instead of self we cam use any word it act as a self i.e. referance
        object.name = name
        object.age = age

    def myFun(abc):
        print("Hello my name is "+abc.name)
        print("and my age is ",abc.age)
p1 = Person("Suraj", 21)
p1.myFun()