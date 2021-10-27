from core import cash_withdraw, verify_pin

opening_balance = 100
current_pin = 1234
attempts = 3
    
while attempts != 0:
    Enter_pin = int(input("Enter your 4-digit passcode to log in: "))
    if verify_pin(current_pin, Enter_pin) is False:
        attempts -= 1
        print("Incorrect entry.You've {} attempts remaining".format(attempts))

        if attempts == 0:
            print("Card blocked! Please visit nearest branch to reactivate pin")

    elif Enter_pin == current_pin:
            print("Welcome to NatWest!")
            break


while True: 
    print("""
  1. Check A/C Balance
  2. Cash Withdraw
  3. Exit
  """)
    choice = int(input("Please Enter Choice: "))
    if choice == 1:
        display_balance(opening_balance)
    elif choice == 2:
        amount = int(input("Enter Withdrawal Amount: "))
        try:
          print('Your account balance is £{}'.format(opening_balance))  
          opening_balance = cash_withdraw(opening_balance, amount)
          print("Your updated account balance is £{}".format(opening_balance))
        except ValueError as err:
          print(err)
          print("Enter another amount to withdraw")
    elif choice == 3:
        print("goodbye")
        break
