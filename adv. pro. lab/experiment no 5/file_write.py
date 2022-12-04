# "a"- will append the end of file 
# "w"- will overwrite any existing contentnt

# 1- appending
f = open("sample2.txt", "a")
f.write("....This content is appended to this file....")
f.close()
#open and read the file after appending
f = open("sample2.txt", "r")
print(f.read())

# 2- writing
f = open("sample2.txt", "w")
f.write("This text is overwritten to file.....")
f.close()
# #open and read file after overwritten
f = open("sample2.txt", "r")
print(f.read())
