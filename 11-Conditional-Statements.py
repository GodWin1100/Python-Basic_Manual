# Relational condition
# > lhs greater than rhs
# < lhs less than rhs
# >= lhs greater than equal to rhs
# <= lhs less than equal to rhs
# \ != lhs not equal to rhs
# == rhs is equal to lhs

# Logical condition #Used for boolean value
#  and   is used when u want more than 1 condition to be valid simultaneously for being executed
#  or    is used when u want any one of the condition to be valid for being executed
#  not   is used to reverse the result or to give opposite output
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nCONDITIONAL STATEMENTS\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# Conditional statements-- if-else-elif

print("\n")
if 5 > 3:  # to check condition and if it is right
    print("hello")
print("\n")

if 3 > 5:
    print("false")
else:  # if statement or condition is false then this will be executed
    print("5 is greater than 3")
print("\n")

if 5 > 3:
    print("5 is greater than 3")
else:  # if statement is true then else will not be executed
    print("lol")
print("\n")

if 6 > 7:
    print("6 is greater than 7")
elif 8 > 3:  # elif means else syntax with condition it means it will ony execute if given condition is true
    print("8 is greater than 3")
print("\n")

age = 16
if age < 13:
    print("you are young")
elif age < 18 and age > 13:
    print("on the way to adult")
else:
    print("welcome to reality")

# nested if-else
print("\nthis is nested if-else")
age = 18  # change age to check nested if-else
son_of = "mla"  # change son_of to check nested if-else
if age >= 18:
    if son_of == "mla":
        print("VIP Treatment")
    else:
        print("welcome to reality")
else:
    print("you are still young")
