print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nFUNCTIONS\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# syntax ====> def function_name (parameters or can be empty or variable):
# we don't have to define data-type for variable in function in python
# function work as a call function it means it will only be executed when it is call for calling syntax ====> function_name()
print("\n")


def welcome():  # function is defined
    print("Hello World!!!")


welcome()  # function is called for execution
print("\n")


def greeting(name):  # variable is passed in the function parameter
    print("Hola " + name + "!!!")


greeting(
    "Shivam"
)  # while calling the function you should also define the content of element for execution or else it will not be executed
print("\n")

# Passing function as a parameter
def seeoff(name2):
    return "Sayonara " + name2


def Identity():
    return "GodWin"


print(seeoff(Identity()))
print("\n")


def addition(a, b):
    print("addition of ", a, "+", b, " is", a + b)


addition(5, 10)
print("\n")

# RETURN
def returnsub(a, b):
    return (
        a - b
    )  # return is used for associating the value with some variable and once return is encounter further execution of code is stopped
    print("hello")  # this will not be executed


sub = returnsub(10, 5)  # value or return will be stored in the variable where function is called
print(sub)

# variable or content of the function can not be called directly without calling the function

# Positional and keyword parameters


# ? parameter after * are keyword parameter they can only be passed by explicitly specifying argument
def func1(pos1, pos2, *, kw1, kw2):
    print(pos1, pos2)
    print(kw1, kw2)


#! func1(1, 2, 3, 4) WRONG
#! func1(kw1=3, 1, 2, kw2=4) Keyword argument should be passed at last positions
func1(1, 2, kw1=3, kw2=4)

# ? Parameter before / are positional and those cannot be passed by specifying keyword
def func2(pos1, pos2, /, strict_pos1, strict_pos2):
    print(pos1, pos2)
    print(strict_pos1, strict_pos2)


func2(5, 6, strict_pos2=8, strict_pos1=9)


# * Other argument before * and after / are normal parameter which can be passed as argument by specifying keywords or as positional arguments
