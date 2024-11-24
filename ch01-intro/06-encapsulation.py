"""
06-encapsulation.py: Python script to demonstrate OOP concept encapsulation.

Description:
    This script contains class definition BankAccount, and demontstrates encapsulation with its private fields
    __account_number and __balance.
Usage:
    `python 06-encapsulation.py`
Arguments:
    None

Author:
    Tuna Cinsoy

Date:
    2024-11-24

Version:
    1.0.0

License:
    MIT License
"""


class BankAccount:
    def __init__(self, account_number: str, balance: float):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:

        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            return False

    # Adding extra layer of security, only a specific user with an account_number can view its balance
    def get_balance(self, account_number) -> str:
        if account_number != "123456789":
            return f"You are not authorized to view this data."
        else:
            return f"Your account has {self.__balance}$ at the moment."


my_account = BankAccount("123456789", 1000)

my_account.deposit(50)

my_account.withdraw(100)
print(my_account.get_balance("123456789"))  # prints 950

print(
    my_account.get_balance("9123912939")
)  # prints You are not authorized to view this data.
