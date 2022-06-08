# Basic File Operation using Python
# program cannot be execute more than one time as file name will keep on changing at every code so if want to run take a look at name change and do the need full
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nREADING FILE\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
test = open("22-basic.txt")  # open() syntax is used to open file for python
print(test.read())  # variable_name.read() is ued to read the file which is open in that particular variable_name
print(
    test.tell()
)  # tell() syntax is used to know the position of cursor in the text file which is opened by python it also counts \n=2(used for new line)
print(test.read())  # this will print nothing as cursor is at the end of the sentence
test.seek(0, 0)  # this bring cursor back to starting postion
help(
    test.seek
)  # first integer parameter indicates number of byte to be moved while second parameter is reference for whence
print(test.tell())
print(test.read())
test.close()  # this will close the file which was opened by open() syntax


print("\n\n\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nEDITING IN FILES\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# editing in file that is only appending(write) and reading
print("\nThis is for writing")
test = open(
    "22-basic.txt", "w"
)  # second parameter is used for specific purpose by default it is r. r=reading,w=writing,wb+=open file for both writing and reading and will overwrite the existing file
test.write("\n This line is typed in python")  # write function will overwrite if it already exist
test.close()
test = open("22-basic.txt")
print(test.read())
test.close()

print("\nThis is for Appending")
test = open("22-basic.txt", "a")  # here a stands for append
test.write(
    "\nThis line is added by python using append"
)  # this line will keep on adding for number of times u run this code
test.close()
test = open("22-basic.txt")
print(test.read())
test.close()
test = open(
    "22-basic.txt", "a+"
)  # here a+ means we can read the file too and same with w+ it means write which is readable too
test.write("\nSecond time adding")
print(test.read())  # here it is readable too

print("\nThis is for Copying File")
import os  # we need to import os for copying file

test = open(
    "22-basic.txt"
)  # if u run this whole code again make sure to rename the open()syntax as file name is changed
test.close()
os.rename("22-basic.txt", "22-Text.txt")  # before renaming file we need to close the file for changes

import os

filename = input("Enter your filename : ")
os.rename("Newname", filename)

import os

file = open("22-change3")
newfile = open("22-Copieddata.txt", "w")
newfile.write(file.read())  # this means newfile will be written with the content of file which is called by fileread()
newfile.close()
file.close()

file = open("22-Copieddata.txt")
print(file.read())
