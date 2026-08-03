from db import users
from emailsend import singleEmailSend
#get current balance function
def balance(account:int)->str:
    print("User in balance page")
    curr_balance=users[account]['balance']
    singleEmailSend(to_email=users[account]['email'],subject="Checking Balance",body=f"Current balance is :{curr_balance}")
    return f"Current Balance is:{curr_balance}"