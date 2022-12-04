# 1-list
a = [10,20,30,40]
print("a[3]=",a[3])
print("A[0]=",a[0])
print("a[1] to a[3] ==>",a[1:3])
print("from -- to all==>",a[0:])
# printing data type of a
print(type(a))
a[2]= 17#replacing 30 with 17
print(a)

# 2-Touple
t = (5,'welcome',1+3J)
print("t[1]==>",t[1])
print("all==>",t[0:])
print(type(t))

# 3-Dictionary
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print(dict['one']) # Prints value for 'one' key
print(dict[2])# Prints value for 2 key
print(tinydict)# Prints complete dictionary
print(tinydict.keys())# Prints all the keys
print(tinydict.values())# Prints all the values

# 4-Set
myset ={'apple','banana','mango'}
print(myset)
print(type(myset))
myset.add('orange') #adding elemnt to existing set
print(myset)
for x in myset:print(x)#it will print all elements in set as a list
print('banana' in myset) #it will return True
myset.remove('apple')#removing element from set
print(myset)

