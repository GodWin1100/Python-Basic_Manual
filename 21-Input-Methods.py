print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nINPUT METHODS\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
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

print("\nUser input for making a list")
list = []  # we have created an empty list
n = int(input("Enter number of items in your list : "))  # we have asked user of number of items in his/her list
for i in range(0, n):  # we used for loops for n-times for taking input of items by user
    item = input("Enter your list item : ")
    list.append(item)  # append(adding) the item in the empty list which we had created before
    print(list)
print("\n\n\nYOUR LIST IS COMPLETE\nList content are ", list)

print("\nUsing while loop\n")
shopitems = []
maxlength = 8  # we could take user input as seen in for loop
while len(shopitems) < maxlength:  # checking length of shopitems list with len() function
    item = input("Enter what you want to BUY : ")
    shopitems.append(item)
    print(shopitems)
print("\n\n\nDone with your List of Items\n\n")
print("Your list consists of : ", shopitems)

print("\nUser input for creating Dictionary")
dict = {}  # initialized an empty dictionary
max = int(input("Enter number of elements for dictionary : "))
for i in range(0, max):
    key = input("Enter person name : ")
    value = input("Enter item : ")
    dict[key] = value  # we use this to append a key_value pair in dictionary
    print(dict)
    print("\n")
print("\n\n\nItems in Dictionary are :\n", dict)

print("\nUsing while loop\n")
shopitems = {}
maxlength = int(input("Enter number of items you want to shop : "))
while len(shopitems) < maxlength:
    key = input("Enter the Name of Person : ")
    value = input("Enter the Item Name : ")
    shopitems[key] = value
    print(shopitems)
    print("\n")
print("\n\n\nDone with Dictionary of items\n\n")
print(shopitems.keys())
print(shopitems.values())
print(shopitems)

print("\nUser input conditional statement")
age = int(input("Enter your age to check whether you are eligible for voting or no : "))
if age >= 0 and age < 12:
    print("Hey champ! You are still too young for voting")
elif age >= 12 and age < 18:
    print("Just a few more years to go...")
elif age >= 18:
    print("You are eligible to vote")
else:
    print("Wrong input")

print("\nUser input for function with parameters")
radius = float(input("Enter radius of circle : "))


def circle(r):
    print(3.14 * r * r)


print("Area of circle with radius ", radius, " is ")
circle(radius)

print("\nUser input for Class")


class circle:
    def __init__(self, r):
        self.radius = r

    def area_circle(self):
        print("Area of circle is ", self.radius * self.radius * 3.14)

    def perimeter_circle(self):
        print("Perimeter of circle is ", self.radius * 2 * 3.14)


radius = int(input("Enter radius of circle : "))
option = int(
    input(
        "Enter 1 for Area of circle\nEnter 2 for Perimeter of cirlce\nEnter 3 for Area and Perimeter oc circle\n Your Choice: "
    )
)
c = circle(radius)
if option == 1:
    c.area_circle()
elif option == 2:
    c.perimeter_circle()
elif option == 3:
    c.area_circle()
    c.perimeter_circle()
else:
    print("Wrong Option Selected")
