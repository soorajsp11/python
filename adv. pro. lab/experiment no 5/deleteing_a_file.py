# to delete a file you must have import OS module
import os
os.remove("sample3.txt")

# cheack if file exist
if os.path.exists("sample3.tx"):
    os.remove("sample3.txt")
else:
    print("file does not exist...!")

# delete folder
os.rmdir("abcd")
# folder only can be deleted if it is emplty(place any file in folder abcd and look result)