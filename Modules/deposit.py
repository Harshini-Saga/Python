from db import users
#deposit
def deposit(account:int,deposit_amount:int)->str:
    print("User in deposit page")
    users[account]['balance']+=deposit_amount
    return f"{deposit_amount} deposit successful and current balance is :{users[account]['balance']}"