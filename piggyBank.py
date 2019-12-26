balance = 0
last_transaction = 0

def show_statement():
    print("Current Balance:", balance)
    print("Last Tansaction:", last_transaction)

def deposit(amount):
    global balance, last_transaction
    if amount <= 0:
        return False
    balance += amount
    last_transaction = amount
    show_statement()
    return True
    
def withdraw(amount):
    global balance, last_transaction
    if amount > balance or amount < 0:
        return False
    balance -= amount
    last_transaction = -amount
    show_statement()
    return True
    
print("Welcome to PiggyBank!")

while True:
    print("Press:\n1. Check Statement\n2. Deposit Money\n3. Withdraw Money")
    choice = int(input())

    if choice == 1:
        show_statement()
    elif choice == 2:
        print("Enter the amount you want to desposit:")
        amount = float(input())
        done = deposit(amount)
        if not done:
            print("Illegal amount to deposit.")
    elif choice == 3:
        print("Enter the amount you want to withdraw:")
        amount = float(input())
        done = withdraw(amount)
        if not done:
            print("Amount to withdraw is greater than currrent balance.")   