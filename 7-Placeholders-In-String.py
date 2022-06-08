print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nPLACEHOLDERS IN STRING\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# placeholders in string
holder1 = "%s is good guy"  # here % means place is reserved and character beside % is data type
print("\n")
print(holder1)  # will print only holder variable
print(holder1 % "shivam")  # will print string at the place of %s where s stands for string
print(holder1)  # it will be same, as placeholder works only when it is called
print(holder1 % "458")  # this will also print integer as string
print(holder1 % 85)  # will print it as string

print("\n")
holder2 = "my id number is %d"
print(holder2)
print(holder2 % 58)  # this will print integer at the place of %d
# ! print(holder2%'lol') #this will show error as it is integer type and we have given input of string

print("\n")
holder3 = "%s is %d years old"
print(holder3)
print(
    holder3 % ("Shivam", 18)
)  # for multiple data type the given input should be followed in same data type sequence and syntax should be followed
print(
    "%s is my first name and %s is my last name while my date of birth is %d/%d/%d"
    % ("Shivam", "Panchal", 11, 10, 2000)
)  # this can be written like this too

print("\n")
name = "Shivam"
age = 18
print(holder1 % name)
print(holder2 % age)
print(
    holder3 % (name, age)
)  # placeholder can be another variable too but with same data type stored in respective variable with respect sequence

print("\n")
greet = "hola"
bye = "sayonara"
print("Hello = {}, Bye = {}".format(greet, bye))  # here we use {} instead of %_DATATYPE_ to keep it generalized
print("Bye = {1}, Hello = {0}".format(greet, bye))  # you can assign index also
