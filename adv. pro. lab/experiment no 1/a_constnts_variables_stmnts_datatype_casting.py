#experiment 1.a_program for constats,variables,statements expression,data type and type casting
#this is comment
'''this is
multiline comment'''
#variables
a=10;
b=20;

#statements
print('a=',a,'b=',b);

#expressions
sum=a+b;
print('addition is:',sum);

#data types
'''1-number'''
a1=25;
a2=3.25;
a3=3+4j;
print(type(a1));
print(type(a2));
print(type(a3));
'''2- list'''
a4=[10,20.13,'i love my India'];
print('a4=',a4);
print(a4[0:2]);
print('data type of a4',type(a4));
'''3-Touple'''
t = (5,'program', 1+3j)
print("t[1] = ", t[1])
print('data type of t',type(t));
'''4-string'''
s='we are the peoples of India'
print(s);
print(s[4]);
print(s[11:18]);
print('data type of s is==>',type(s));
'''5-set'''
a5= {5,2,3,1,4}
print("a5 = ", a5)
print('data type of a',type(a5));
'''6-dictinory'''
d = {1:'value','key':2}
print(type(d))
print("d[1] = ", d[1])
print("d['key'] = ", d['key']);

#type conversion or casting
'''1-Implicit type conversion'''
'''int to float'''
num_int = 123
num_flo = 1.23
num_new = num_int + num_flo
print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))
print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))
'''2-Explicit type conversion'''
num_int = 123
num_str = "456"
print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))
num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))
num_sum = num_int + num_str
print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))





