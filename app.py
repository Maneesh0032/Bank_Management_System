#Operations
def login(account:int, password:str)->bool:
    #Check if the account and password are correct
    #Return True if correct, False otherwise
    pass

def register(username:str,email:str, password:str,deposited_amount:int):
    #Check if the username and email are unique
    #If unique, create a new account and return True
    #Otherwise, return False
    pass

def get_balance(account:int)->int:
    #Return the balance of the account
    pass

def withdraw(account:int, withdraw_amount:int)->str:
    #Check if the account has enough balance
    #If enough, deduct the amount from the balance and return True
    #Otherwise, return False
    pass

def deposit(account:int, deposit_amount:int)->str:
    pass

def transfer(from_account:int, to_account:int, transfer_amount:int):
    pass

def mini_statement(account:int)->list[dict]:
    pass

def logout():
    pass

#main function
if __name__ == "__main__":
    print("Welcome to small scale Bank System")
    print("select your operation \n1. Register \n2. Login \n3. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        username=input("Enter your username: ")
        email=input("Enter your email: ")
        password=input("Enter your password: ")
        deposited_amount=int(input("Enter the amount to deposit: "))
        if register(username, email, password, deposited_amount):
            print("Registration successful")
        else:
            print("Registration failed")
    elif choice==2:
        account=int(input("Enter your account number: "))
        password=input("Enter your password: ")
        if login(account, password):
            print("Login successful")
            while True:
                print("select your operation \n1. Get Balance \n2. Withdraw \n3. Deposit \n4. Transfer \n5. Mini Statement \n6. Logout")
                choice=int(input("Enter your choice: "))
                if choice==1:
                    balance=get_balance(account)
                    print(f"Your balance is {balance}")
                elif choice==2:
                    withdraw_amount=int(input("Enter the amount to withdraw: "))
                    if withdraw(account, withdraw_amount):
                        print("Withdraw successful")
                    else:
                        print("Insufficient balance")
                elif choice==3:
                    deposit_amount=int(input("Enter the amount to deposit: "))
                    if deposit(account, deposit_amount):
                        print("Deposit successful")
                    else:
                        print("Deposit failed")
                elif choice==4:
                    to_account=int(input("Enter the account number to transfer to: "))
                    transfer_amount=int(input("Enter the amount to transfer: "))
                    if transfer(account, to_account, transfer_amount):
                        print("Transfer successful")
                    else:
                        print("Transfer failed")
                elif choice==5:
                    statement=mini_statement(account)
                    for transaction in statement:
                        print(transaction)
                elif choice==6:
                    logout()
                    print("Logout successful")
                    break
                else:
                    print("Invalid choice")
        else:
            print("Login failed")
    elif choice==3:
        print("Thank you for using our bank system. Goodbye!")
    else:
        print("Invalid choice")

