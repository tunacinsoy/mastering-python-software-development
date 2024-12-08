"""
Abstract:


Description:
    This script contains class definition BankAccount, and demonstrates encapsulation with its
    private field __account_number and protected field _balance.

    Private members are similar to protected members,
    but the difference is that class members declared as private cannot be accessed outside the class, nor by any derived class.
    In other words, private members are only accessible within the class where they are declared.

Usage:
    `python <file_name>`

Arguments:
    None

Author:
    Tuna Cinsoy

License:
    MIT License
"""

from functools import reduce

# Lambda function with one input parameter
square = lambda x: x**2
print(square(5))  # 25

# Lambda function with two input parameters
multiply = lambda x, y: x * y
print(multiply(4, 5))  # 20

# Map function applies a given function as first parameter, to an iterable (passed as second parameter)
# and returns an object of map. We can do explicit casting to list type, and then we can have another list to store
# the processed values.

# Map function with lambda function inside
nums = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x**2, nums))
print(squared_nums)  # [1,4,9,16,25]
print(type(map(lambda x: x**x, nums)))  # <class 'map'>


def celsius_to_fahrenheit(degree: float) -> float:
    return degree * 9 / 5 + 32


# Map function with another function passed
celc_degrees = [22, 23, 24, 25, 26]
fahr_degrees = list(map(celsius_to_fahrenheit, celc_degrees))
print(fahr_degrees)  # [71.6, 73.4, 75.2, 77.0, 78.8]


# Filter function filters the elements of an iterable according to the boolean statement
# passed as first input parameter
nums = [1, 2, 3, 4, 5, 6]

# Filter function with lambda function inside
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # [2,4,6]


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:  # 2 and 3 are prime
        return True
    if n % 2 == 0 or n % 3 == 0:  # Eliminate multiples of 2 and 3
        return False
    i = 5
    while i * i <= n:  # Check factors up to √n
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # Skip even numbers and multiples of 3
    return True


# Filter function with another function inside
prime_nums = list(filter(is_prime, range(1, 100)))
print(
    prime_nums
)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


# The reduce() function applies a function of two arguments cumulatively to the items of an iterable,
# reducing it to a single value.
result_with_reduce = reduce(lambda x, y: x * y, nums)
print(result_with_reduce)

# This is what reduce does actually.
nums = [1, 2, 3, 4, 5]
result = 1
for num in nums:
    result *= num
print(result)


# Reduce with regular function
def concatanate(s1, s2):
    return s1 + "-" + s2


names = ["Tuna", "Wika"]

concat_string = reduce(concatanate, names)

print(concat_string)
