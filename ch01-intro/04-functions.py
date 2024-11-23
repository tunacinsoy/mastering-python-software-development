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


greetMessage = greet("tuna")
print(greetMessage)

age = calculate_age(1999)
print(age)
