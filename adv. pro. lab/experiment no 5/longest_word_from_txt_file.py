# to fing longest words in txt file
from http.client import LENGTH_REQUIRED


n = int(input("enter least no of characters that words contains:"))
f = open("sample.txt", "r")
s = f.read()
#make a list according to words seprated by space
L = s.split()
print(L)
for i in L:
    if (len(i)>n):
        print(i)


# to fing biggest word among the all words
print("\nmaximum length words are:",max(L,key=len))

#to fing min length word among the all words
print("\nminimum legth words are:",min(L,key=len))