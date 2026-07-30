from db import users
#Login function 
def login(account:int,password:str)->bool:
    print("User in login page")
    if account in users:
        if users[account]['password']==password:
            return True
        return False
    return False