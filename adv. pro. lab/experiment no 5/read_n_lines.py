# To read first n lines of a file

n = int(input("enter no of lines you want to read:"))
f = open("sample.txt", "r")
print("\nfirst",n," lines are .....\n")
for line in (f.readlines() [:n]):
    print(line,end="")
f.close()

# To read last n lines of a file

n = int(input("\nenter no of lines you want to read:"))
f = open("sample.txt", "r")
print("\nlast",n," lines are .....\n")
for line in (f.readlines() [-n:]):
    print(line,end="")
f.close()
