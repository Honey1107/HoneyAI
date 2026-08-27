# 03_Raising_Exceptions
class InsufficientBalanceError(Exception):
    pass


# Real values
account_balance = 5000
withdraw_amount = 7500

try:
    # Check whether the account has enough money
    if withdraw_amount > account_balance:
        raise InsufficientBalanceError(
            f"Insufficient balance. "
            f"Available: ₹{account_balance}, "
            f"Requested: ₹{withdraw_amount}"
        )

    # Deduct the withdrawal amount
    account_balance -= withdraw_amount

    print(f"Withdrawal successful.")
    print(f"Remaining balance: ₹{account_balance}")

except InsufficientBalanceError as e:
    print(f"Transaction failed: {e}")