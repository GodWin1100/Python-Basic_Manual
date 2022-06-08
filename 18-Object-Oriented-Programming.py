print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nOBJECT-ORIENTED PROGRAMMING\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# object oriented programming
print("\n")


class simple:  # simple class  syntax===> class class_name:
    pass


p = simple()
print(p)

print("\nNormal class")


class Info:
    def name(
        self,
    ):  # parameter cannot be empty or null in function of a class as class object is passed through function parameter
        print("Shivam")

    def age(self):
        print("18")


myself = Info()  # here myself is an object created which can approach function of class Info()
print(myself.name())  # to call an function inside a class we use object_name.function_name()
print(myself.age())

print("\nClass with parameter")


class infocard:
    def __init__(
        self, name, age
    ):  # we use __init__ for taking parameter in function of a class. DOUBLE UNDERSCORE(__) both side of init
        self.n = name  # we use self.variable_name to store it in the class to call it anywhere in the class.
        self.age = age  # variable_name can be anything but they should store the parameter_variable

    def NAME(self):
        print("Your name is ", self.n)

    def AGE(self):
        print("Your age is ", self.age)


icard = infocard("Shivam", 18)
print(icard.NAME())
print(icard.AGE())
