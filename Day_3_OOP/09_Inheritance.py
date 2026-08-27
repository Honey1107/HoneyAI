# 09_Inheritance
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner            # public
        self._account_type = "SAVINGS"  # protected (convention: internal use)
        self.__balance = balance        # "private" (name-mangled)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance


account = BankAccount("Asha", 1000)
print("Initial balance:", account.get_balance())

account.deposit(500)
print("After deposit:", account.get_balance())

account.withdraw(200)
print("After withdrawal:", account.get_balance())

try:
    account.withdraw(10_000)
except ValueError as e:
    print("Error caught:", e)

# Direct access to the "private" attribute fails as expected
try:
    print(account.__balance)
except AttributeError as e:
    print("AttributeError as expected:", e)

# But it's not truly unreachable -- name mangling, not real privacy
print("Name-mangled access (for demonstration only):", account._BankAccount__balance)