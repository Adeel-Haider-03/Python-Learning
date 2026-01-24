
# we can make variables and methods private by prefixing their names with double underscores (__).
# provate variables and methods cannot be accessed directly from outside the class.

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private variable
        self.__balance = balance  # private variable

    def __display_account_info(self):  # private method , can only be called by other methods within the class
        return f'Account Number: {self.__account_number}, Balance: ${self.__balance}'

    def getter(self):
        return self.__display_account_info()
    
    def setter(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            return "Invalid amount. Balance cannot be negative."

account=BankAccount("123456789", 1000)
print(account.getter())  # Accessing private method via public method

account.setter(1500)  # Modifying private variable via public method
print(account.getter())