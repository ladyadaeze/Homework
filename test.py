from core import cash_withdraw, verify_pin

assert cash_withdraw(1000, 100) == 900, "Cash not properly withdrawn"
assert cash_withdraw(456, 6) == 450, "Cash not properly withdrawn"
assert verify_pin("4567", "4567") is True, "Pin Verifcation not accurate"
assert verify_pin("4568", "4567") is False, "Pin Verifcation not accurate"

try:
    cash_withdraw(100, 1000)
    assert False, "Should Throw Exception"
except ValueError as Err:
    assert True    


print("Everything passed")   