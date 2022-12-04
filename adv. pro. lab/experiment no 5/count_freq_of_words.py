from itertools import count

f = open("sample.txt", "r")
word = input("enter the word to be searched:")

s=f.read() # stores the string is s
#make a list
L = s.split()
count=0
for i in L:
    if(i==word):
        count+=1
print("word {} occured {} times".format(word,count))
f.close()