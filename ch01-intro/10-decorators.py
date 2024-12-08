"""
Description:
    The aim of this script is to understand decorators.

Usage:
    `python <file_name>`

Arguments:
    None

Author:
    Tuna Cinsoy

License:
    MIT License
"""


# The uppercase_decorator function is defined to take another function (func) as an argument.
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


#  When greet() is called,
#  it actually calls the wrapper function inside the decorator,
#  which in turn calls the original greet function, modifies its result, and returns the modified result.
@uppercase_decorator
def greet():
    return "hello world!"


print(greet())


def repeat(times):
    def decorator(func):

        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def say_hello(name):
    print(f"Hello {name}!")


# Here's what happens step-by-step when say_hello("Tuna") is called:
# The wrapper function is executed.
# Inside the wrapper, a loop runs three times (as specified by times).
# In each iteration of the loop, the original say_hello function is called with the argument "Tuna",
# printing "Hello Tuna!" each time.

say_hello("Tuna")
