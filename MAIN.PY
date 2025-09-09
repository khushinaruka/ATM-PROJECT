from atm_operations import deposit, withdraw, check_balance

balance = 20000
print("Options: deposit, withdraw, checkbalance")
useroption = input("Enter your option: ").lower()

if useroption == "deposit":
    amount = int(input("Enter amount to deposit: "))
    balance = deposit(balance, amount)
elif useroption == "withdraw":
    amount = int(input("Enter amount to withdraw: "))
    balance = withdraw(balance, amount)
elif useroption == "checkbalance":
    check_balance(balance)
else:
    print("Invalid option.")
