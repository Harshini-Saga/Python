from db import users
#get current balance function
def balance(account:int)->str:
    print("User in balance page")
    curr_balance=users[account]['balance']
    return f"Current Balance is:{curr_balance}"