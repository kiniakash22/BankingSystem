from prettytable import PrettyTable

account_no = 1000

def generate_account_no():
    global account_no
    account_no += 1
    return account_no


class Bank:
    def __init__(self):
        self.account_list = []
        pass

    def add_account(self, account):
        self.account_list.append(account)

    def check_if_account_exists(self, account_no):
        for acc in self.account_list:
            if acc.account_no == account_no:
                return acc
        return False

class Account:
    def __init__(self):
        global account_no
        self.last_transaction = 0
        self.last_transaction_history = []
        self.balance = 0
        self.balance_history = []
        self.account_no = generate_account_no()

    def show_statement(self):
        print("Current Balance:", self.balance)
        print("Last Tansaction:", self.last_transaction)

    def deposit(self, amount):
        # global balance, last_transaction
        if amount <= 0:
            return False
        self.balance += amount
        self.last_transaction = amount
        self.last_transaction_history.append(self.last_transaction)
        self.balance_history.append(self.balance)
        self.show_statement()
        return True
        
    def withdraw(self, amount):
        # global balance, last_transaction
        if amount > self.balance or amount < 0:
            return False
        self.balance -= amount
        self.last_transaction = -amount
        self.last_transaction_history.append(self.last_transaction)
        self.balance_history.append(self.balance)
        self.show_statement()
        return True

    def print_account_details(self):
        print("Account No.: ", self.account_no)
        self.show_statement()

    def print_balance_sheet(self):
        print("-"*60)
        self.balance_sheet_table = PrettyTable(["Tr No.", "Credit", "Debit", "Balance"])
        for i in range(len(self.balance_history)):
            if self.last_transaction_history[i] < 0:
                self.balance_sheet_table.add_row([i + 1, -self.last_transaction_history[i], '', self.balance_history[i]])
            else:
                self.balance_sheet_table.add_row([i + 1, '', self.last_transaction_history[i], self.balance_history[i]])
        print(self.balance_sheet_table)


bank = Bank()

while True:
    print("\n", "__*"*5, "Welcome to Maybe Bank!", "*__"*7)
    outer_choice = int(input("\nPress:\n1. To create a new account\n2. Login to your account\n3. Exit\n\nEnter your choice: "))

    if outer_choice == 1:
        acc = Account()
        print("-"*60,"\nAccount successfully created with following details:")
        print("-"*60)
        acc.print_account_details()
        bank.add_account(acc)
        print("-"*60)
        continue

    elif outer_choice == 2:
        print("-"*60)
        account_no = int(input("Enter your account number: "))
        acc = bank.check_if_account_exists(account_no)
        if acc:
            while True:
                print("-"*60)
                print("Welcome account number", acc.account_no, "\n\nPress:\n1. Check Statement\n2. Deposit Money\n3. Withdraw Money\n4. Show Balance Sheet\n0. Logout\n\nEnter your choice: ")
                inner_choice = int(input())

                if inner_choice == 1:
                    print("-"*60)
                    acc.show_statement()
                    print("-"*60)

                elif inner_choice == 2:
                    print("Enter the amount you want to desposit:")
                    amount = float(input())
                    done = acc.deposit(amount)
                    if not done:
                        print("Illegal amount to deposit.")
                elif inner_choice == 3:
                    print("Enter the amount you want to withdraw:")
                    amount = float(input())
                    done = acc.withdraw(amount)
                    if not done:
                        print("Amount to withdraw is invalid.") 
                elif inner_choice == 4:
                    acc.print_balance_sheet()
                    pass
                
                elif inner_choice == 0:
                    break  

        else:
            print("\n", "x-"*7, "Account does not exists!!!", "-x"*7)
            continue

    elif outer_choice == 3:
        ask_again = input("Do you really want to exit? (Y/N): ").upper()
        if ask_again == "Y":
            break
        else: continue



# input
# 1
# 2
# 1001
# 2
# 300
# 3
# 120
# 2
# 5000
# 2
# 450
# 3
# 50
# 4
# 0
# 1
# 2
# 1002
# 2
# 3000
# 3
# 1200
# 2
# 50000
# 2
# 4500
# 3
# 500
# 4
