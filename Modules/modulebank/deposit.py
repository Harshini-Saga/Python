from db import users
from emailsend import singleEmailSend
#deposit
def deposit(account:int,deposit_amount:int)->str:
    print("User in deposit page")
    users[account]['balance']+=deposit_amount
    singleEmailSend(to_email=users[account]['email'],subject="Deposit Alert",body=f"{deposit_amount} deposit successful and Current balance is :{users[account]['balance']}")
    return f"{deposit_amount} deposit successful and Current balance is :{users[account]['balance']}"