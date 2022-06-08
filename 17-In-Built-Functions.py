print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nIN-BUILT FUNCTION\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# built-in functions
# absolute     #absolute function which is used as mod of mathematics
print("\nAbsolute")
print(abs(-34))
print(abs(45))

# boolean     #boolean is just like truth table. 0/None value in bool is False and rest other value is True
print("\nBoolean")
print(bool(0))
print(bool(1))
print(bool(-54))
print(bool(102.25))
print(bool(None))
print(bool([]))
print(bool("ashdb"))

# dir     #just like a directory of function which gives the possible function operation on given data
print("\nDir")
print("\non hello world")
print(dir("hello world"))
print("\non 5")
print(dir(5))

# help     #gives instruction or purpose of a particular function
print("\nHelp")
var = "hello"
print(help(var.upper))
print(var.upper())

# eval     #takes in string and executes the string as a python code
print("\nEval")
string = "print('this is a function as a string')"
print(string)
print(eval(string))
print(eval("print('direct input')"))
# exec (execute) is also a in-built function which is similar to eval but exec can execute multiple lines
print("\nExec")
string = "print('hello nice to meet you');print('Can we be friends??')"
print(exec(string))
print("\n")

# changing data type
print("\nChange of data types")
a = 154
print("Type of a", type(a))
print("Converted to string : ", str(a), type(str(a)))
print("Converted to float : ", float(a), type(float(a)))
print("Converted to binary : ", bin(a), type(bin(a)))
print("Converted to hexadecimal : ", hex(a), type(hex(a)))
print("Converted to octal : ", oct(a), type(oct(a)))
var = "8"  # string cannot be change into integer or float if string content is not 0-9 numbers
print(int(var))
print(float(var))
f = 158.3552
inti = int(f)
print("Converted float ", f, type(f), " to integer : ", inti, type(inti))


# len (length)
print("\nNumber of element")
state = "How many numbers are there?"
print(state)
print(len(state))  # this will count spacebar too
list = [5, 4, 8, 5, 4, "ksdh"]
print(len(list))
print("\n")

# sum function
array = [5, 8, 4, 8]
print(array)
print("Sum of given array is ", sum(array))

# use of len
print("\nBasic use of len")
for i in range(0, len(list), 2):
    print(i)
