print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nINHERITANCE\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# inheritance  working just like normal inheritance
# syntax====> class class_name(name_of_class_which_is_to_be_inherited):
print("\n")


class main:  # this ia parent class
    def parent(self):
        print("This is parent")

    def grandparent(self):
        print("This is grand parent")


print("\n")


class subordinate(
    main
):  # this is child class which has inherited parent class # ? in this case it has inherited main class
    def child(self):
        print("This is in subordinate")


trial = subordinate()
print(trial.child())  # we can approach to main class because object_trial is in subrodinate class
print(
    trial.parent(), trial.grandparent()
)  # and we can call main class function because subordinate class has inherited main class function

print("\nOverride method")
# override method
class parent:
    def test(self):
        print("This is in parent")


p = parent()
p.test()


class child(parent):  # inherited parent
    def test(self):  # same function_name as in parent class
        print("This is in child")


c = child()  # the parent function will be override by the function of child if both function name are same
c.test()  # and class_child function will be executed
