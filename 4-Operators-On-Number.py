print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nOPERATORS ON NUMBERS\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# operators on numbers

num1 = 10
num2 = 5
print("\nAddition=", num1 + num2)  # addition
print("\nSubtraction=", num1 - num2)  # subtraction
print("\nDivision=", num1 / num2)  # division gives quotient this will give answer in float i.e. in decimal format
print(type(num1 / num2))
print(
    "\nDivison in Integer Format=", num1 // num2
)  # double division sign will give answer in integer format only without any decimal
print(type(num1 // num2))
print("\nMultiplication=", num1 * num2)  # multiplication
print("\nModulus=", num1 % num2)  # modulus gives remainder
print("\nPower=", num1 ** num2)  # this is used for raising power on a number (base)**(power)

num1 = 52.6
num2 = 27.8
print("\nFloat Values\nDivision=", num1 / num2)
print(
    "Double Division or Integer Division or Floor Division=", num1 // num2
)  # here it will be in float but will show only integer
print(type(num1 // num2))
print("\nModulus=", num1 % num2)
print("\nAddition=", num1 + num2)
print("\nSubtraction=", num1 - num2)

# Compound assignment operators
# can be used with any arithmetic operators
num1 = 5
num2 = 3
print("\ninital value num1 ", num1, " and initial value of num2 ", num2)
num2 += 2  # num2=num2+2
print(num2)
num2 -= 2  # num2=num2-2
print(num2)
num1 *= 2  # num1=num1*2
print(num1)
num1 /= 2  # num1=num1/2
print(num1)
num1 %= 4  # num1=num%4
print(num1)
