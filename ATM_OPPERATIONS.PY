def deposit(balance, amount):
    balance += amount
    print(f"New balance: {balance}")
    return balance

def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount
        print(f"New balance: {balance}")
    else:
        print("Insufficient balance.")
    return balance

def check_balance(balance):
    print(f"Your current balance is: {balance}")
