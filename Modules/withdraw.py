from db import users
def withdraw(account:int,withdraw_amount:int)->str:
    print("User in withdraw page")
    curr_balance=users[account]['balance']
    if curr_balance >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount
        return f"{withdraw_amount} withdraw successful and current balance is :{users[account]['balance']}"
    return "Insufficient Amount"
