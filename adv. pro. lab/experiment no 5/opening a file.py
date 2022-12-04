# f = open("sample.txt") ==> to open a file 

# reding content of file
f = open("sample.txt", "r")
print(f.read())

# to read pirticular no of chatracters from start
f = open("sample.txt", "r")
print("\nreading first 5 characters......")
print(f.read(5))

# to read a single line
f = open("sample.txt", "r")
print("\nreading first line.....")
print(f.readline())

# to read whole file line by line
f = open("sample.txt", "r")
print("\n reading file line by line.....")
for x in f:
    print(x)

# closing file when u finish with it
f.close()

