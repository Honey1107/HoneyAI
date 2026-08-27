# 15_Abstraction
from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        """Every concrete processor must implement this."""
        raise NotImplementedError

    def receipt(self, amount):
        # Concrete (non-abstract) method: shared logic, available to all subclasses
        return f"Receipt: charged {amount} via {self.__class__.__name__}"


class CreditCardProcessor(PaymentProcessor):
    def pay(self, amount):
        return f"Processing ${amount} via credit card (internal Luhn check hidden)."


class UpiProcessor(PaymentProcessor):
    def pay(self, amount):
        return f"Processing ${amount} via UPI (internal bank handshake hidden)."


processors = [CreditCardProcessor(), UpiProcessor()]
for p in processors:
    print(p.pay(100))
    print(p.receipt(100))

# Attempting to instantiate the abstract class directly fails
try:
    PaymentProcessor()
except TypeError as e:
    print("TypeError as expected:", e)
