# to print random line from a text file
import random
f = open("sample.txt", "r") #or     with open("sample.txt", "r") as f ==> no need to f.close()
#make a list of lines
L = f.readlines()
length = len(L)
r1 = random.randint(0, length-1)
print(L[r1])
f.close()