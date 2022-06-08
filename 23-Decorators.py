print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nDECORATORS\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
"""Decorators are syntactic sugar for function which take function as argument and does some pre/post execution and returns the function"""


class Author:
    def __init__(self, name) -> None:
        self.name = name
        self.logged_in = False


def is_authenticated(func):
    def wrapper(user):
        func(user) if user.logged_in else print(403)

    return wrapper


# this will pass blog function as argument to is_authenticated
@is_authenticated
def blog(user):
    print(f"Blog by {user.name}")


author = Author("Writer")
blog(author)
author.logged_in = True
blog(author)

# without using decorator (syntactic sugar)
def like(user):
    print(f"Blog liked by {user.name}")


# just like using decorator
auth_like = is_authenticated(like)

author_2 = Author("Auth")
auth_like(author_2)
author_2.logged_in = True
auth_like(author_2)

# Execution sequence of decorators

print("\n\n UNDERSTANDING OF DECORATOR \n\n")


def decorator(func):
    print("\t> Main Decorator")

    def wrapper(*args, **kwargs):
        print("\t\t>> in wrapper")
        print("\t\t>> args", args)
        print("\t\t>> kwargs", kwargs)
        func(*args, **kwargs)
        print("\t\t>> Execution completed within wrapper")

    print("\t> execution complete of decorator")
    return wrapper


@decorator
def child_fun(one, two, three, four):
    print(f"\t\t\t>>> argument: {one, two, three,four}")
    print("\t\t\t>>> In child function")


child_fun(1, 2, 3, four=4)
