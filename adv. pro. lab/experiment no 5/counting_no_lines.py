# to count no of lines in a text file
f = open("sample.txt", "r") #or     with open("sample.txt", "r") as f ==> no need to f.close()
#make a list of lines
L = f.readlines()
# print(L)

print("no of lines are:", len(L))
f.close()