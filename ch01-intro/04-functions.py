from datetime import datetime


def greet(name):
    return f"Welcome, {name}!"


# Using type hint (:) we specify that birthYear parameter should be type of int
# However, it is not strict, user can also pass a float
# So, we need to check the input parameter's type
def calculate_age(birthYear: int) -> int:
    if type(birthYear) is not int:
        return TypeError(f"Expected integer or float, however got {type(birthYear)}")
    return f"Given that you were born in {birthYear}, your age is {datetime.now().year - birthYear}!"


# TODO: Write a functions that accepts *args and **kwargs
def differentiate_input_types(age, *args, **kwargs):

    # Process age
    if age > 40:
        print(f"time to go home, your age is {age}.")

    # Process *args
    sum = 0
    for arg in args:
        if type(arg) is int:
            sum += arg
        elif type(arg) is float:
            sum += arg
        else:
            print(arg)

    print(f"sum is {sum}.")

    # Process **kwargs
    # Iterate over keys only
    for key in kwargs.keys():
        print(f"current provided kwarg key is: {key}")

    # Iterate over values only
    for val in kwargs.values():
        print(f"current provided kwarg value is: {val}")

    # Iterate over keys and values at the same time
    for key, val in kwargs.items():
        print(key, val)


differentiate_input_types(
    50, 2.0, 3.5, 4, 4, 5, 5, 6, "ahmet", "hulusi", key=15, tornado=23
)
greetMessage = greet("tuna")
print(greetMessage)

age = calculate_age(1999)
print(age)
