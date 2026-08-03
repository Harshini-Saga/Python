from db import users
from emailsend import singleEmailSend
def withdraw(account:int,withdraw_amount:int)->str:
    print("User in withdraw page")
    curr_balance=users[account]['balance']
    if curr_balance >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount
        #sendemail
        singleEmailSend(to_email=users[account]['email'],subject="Withdraw Alert",body=f"{withdraw_amount} withdraw successful and \
                        current balance is :{users[account]['balance']}")
        return f"{withdraw_amount} withdraw successful and current balance is :{users[account]['balance']}"
    return "Insufficient Amount"
