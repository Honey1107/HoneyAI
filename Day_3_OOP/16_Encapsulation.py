# 16_Encapsulation
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        # Unambiguous, developer-facing representation
        return f"Money({self.amount!r}, {self.currency!r})"

    def __str__(self):
        # Friendly, user-facing representation
        return f"{self.amount:.2f} {self.currency}"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        if not isinstance(other, Money) or self.currency != other.currency:
            return NotImplemented
        return self.amount < other.amount

    def __add__(self, other):
        if not isinstance(other, Money) or self.currency != other.currency:
            return NotImplemented
        return Money(self.amount + other.amount, self.currency)

    def __len__(self):
        # Contrived, but demonstrates len() support: whole-currency-unit count
        return int(self.amount)


m1 = Money(20)
m2 = Money(9.5)

print(str(m1))
print(repr(m1))
print(m1 + m2)
print(m1 == Money(20))
print(m2 < m1)
print(len(m1))

wallet = [Money(5), Money(50), Money(1)]
print([str(m) for m in sorted(wallet)])
