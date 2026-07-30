#Login
from login import login
#Register function
from register import register
#withdraw function
from withdraw import withdraw
#deposit
from deposit import deposit
#transfer
from transfer import transfer
#mini statement
from ministmt import ministatement
#logout
from logout import logout
#balance
from balance import balance
#main
if __name__=="__main__":
    print("Welcome to the Mini Bank")
    print("1.Login \n 2.Register")
    choice=int(input("Enter your choice:"))
    if choice==1:
        #Call Login
        account=int(input("Enter your account number:"))
        password=input("Enter your password:")
        login_val=login(account=account,password=password)
        while login_val:
            print("1.Get Balance\n 2.Withdraw \n 3.Deposit \n 4.Transfer \n 5.MiniStatement \n 6.Logout")
            choice=int(input("Enter your choice:"))
            if choice==1:
                #Call Balance functions
                print(balance(account=account))
            elif choice==2:
                amount=int(input("Enter Withdraw Amount:"))
                print(withdraw(account=account,withdraw_amount=amount))
            elif choice ==3:
                amount=int(input("Enter Deposit Amount:"))
                print(deposit(account=account,deposit_amount=amount))
            elif choice==4:
                receiver=int(input("Enter receiver account number:"))
                amount=int(input("Enter Deposit Amount:"))
                print(transfer(from_acc=account,to_acc=receiver,transfer_amount=amount))
            elif choice==5:
                print(ministatement(account=account))
            elif choice==6:
                print(logout())
            else:
                print("Select your choice in between 1-6")
        else:
            print("Invalid Login Credentials")
    elif choice==2:
        #call register
        username=input("Enter Username:")
        email=input("Enter User email id:")
        initial_deposit=int(input("Enter initial deposit amount:"))
        password=input("Enter your new password:")
        register_val=register(username=username,email=email,balance=initial_deposit,password=password)
    else:
        print("Invalid choice,Please select 1 or 2")
