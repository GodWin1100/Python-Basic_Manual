print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nINPUT TYPES\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# input given by user
# input syntax===> input('any_statement to print if u want to') or else input()
print("\n")
any = input(
    "Enter anything "
)  # if data type is not specified before input then every input will be by default an string
print(any)
print(type(any))
number = int(input("Enter only numbers or else encounter a error "))
print(number)
print(type(number))
decimal = float(input("Enter number with decimal " "or integer or else encounter a error "))
print(decimal)
print(type(decimal))
print("\n")

print("Operations")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
mod = num1 % num2
print(add, "<addition\n", sub, "<subtraction\n", mul, "<multiplication\n", div, "<division\n", mod, "<modulus")


print("\n")
# Multiple Inputs
print("Multiple Inputs")
test = input("Enter seperated by spaces : ").split()
print(test)
print(type(test), "length=", len(test))
print(test[0], "=", type(test[0]))

test2 = input("Enter separated by comma : ").split(
    ","
)  # here u need to put comma (,) for 2nd input or else it will consider it as one input only
print(test2)  # if u defined something ele within split such as split('+') then u need to use + for separating it
print(type(test2), "length=", len(test2))
print(test2[0], "=", type(test2[0]))

test3 = [
    int(x) for x in input("Enter Integers only : ").split()
]  # here you can define particular datatype which will be input

print(test3)
print(type(test3), "length=", len(test3))
print(test3[0], "=", type(test3[0]))

test4 = [y for y in input("Enter anything with space separated : ").split()]
print(test4)
print(type(test4), "length=", len(test4))
print(test4[0], "=", type(test4[0]))
