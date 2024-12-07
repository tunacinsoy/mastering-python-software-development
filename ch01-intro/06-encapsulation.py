"""
06-encapsulation.py: Python script to demonstrate OOP concept encapsulation.

Description:
    This script contains class definition BankAccount, and demonstrates encapsulation with its
    private field __account_number and prpotected field _balance.

    Private members are similar to protected members,
    but the difference is that class members declared as private cannot be accessed outside the class, nor by any derived class.
    In other words, private members are only accessible within the class where they are declared.

Usage:
    `python 06-encapsulation.py`

Arguments:
    None

Author:
    Tuna Cinsoy

License:
    MIT License
"""


class BankAccount:
    def __init__(self, account_number: str, balance: float, health: str):

        # Private field: neither can be accessed from subclasses, nor outside
        self.__account_number = account_number
        # Protected Field: can be accessed from subclasses and outside
        self._balance = balance
        # Public Field: can be accessed from subclasses and outside
        self.health = health

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self._balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:

        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False

    # Get method for protected field
    # Adding extra layer of security, only a specific user with an account_number can view its balance
    def get_balance(self) -> str:
        if self.__account_number != "77443322":
            return f"You are not authorized to view this data."
        else:
            return f"Your account has {self._balance}$ at the moment."

    # Get method for private field
    def get_account_number(self) -> str:
        return self.__account_number


tuna_account = BankAccount("123456789", 1000, "healthy")
wiktoria_account = BankAccount("77443322", 1000, "healthy")

# Accessing protected field is permitted from the outside of the class
# However, it shouldn't be in OOP concept
print(tuna_account._balance)  # 1000

# Accessing private field is not permitted from the outside of the class
# print(
#     tuna_account.__account_number
# )  # AttributeError: 'BankAccount' object has no attribute '__account_number'


# This is called name mangling, python changes the private fields' name to include the class name as well,
# so that it becomes a bit more harder to access from outside. despite of this fact, it is still possible.
print(tuna_account._BankAccount__account_number)  # prints 123456789

# Accessing public field is permitted from the outside of the class
print(tuna_account.health)  # Healthy

tuna_account.deposit(50)
tuna_account.withdraw(100)


wiktoria_account.deposit(1000)
wiktoria_account.withdraw(900)

print(tuna_account.get_balance())  # prints You are not authorized to view this data.
print(wiktoria_account.get_balance())  # prints  1100$
