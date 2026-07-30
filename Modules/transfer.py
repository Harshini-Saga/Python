from db import users
#transfer
def transfer(from_acc:int,to_acc:int,transfer_amount:int):
    print("User in transfer page")
    curr_balance=users[from_acc]['balance']
    if curr_balance >= transfer_amount:
        users[from_acc]['balance']-= transfer_amount
        users[to_acc]['balance'] += transfer_amount
        return f"{transfer_amount} Transfer Successful and Current Balance is:{users[from_acc]['balance']}"
    return "Insufficient Amount"