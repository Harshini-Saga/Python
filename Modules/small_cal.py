#importing required modules
#import port module
import addition

#importing function
from subtraction import sub

#importing module with alias name
import multiplication as MUL

#import function with alias name
from division import div as DIV

if __name__=="__main__":
    print("Welcome to Small calculator")
    while True:
        print(" 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            a,b=map(int,input("Enter two numbers separated with space:").split())
            res=addition.add(a,b)
            print(f"Addition of {a} and {b}:{res}")
        elif choice==2:
            a,b=map(int,input("Enter two numbers separated with space:").split())
            res=sub(a,b)
            print(f"Subtraction of {a} and {b}:{res}")
        elif choice==3:
            a,b=map(int,input("Enter two numbers separated with space:").split())
            res=MUL.mul(a,b)
            print(f"Multiplication of {a} and {b}:{res}")
        elif choice==4:
            a,b=map(int,input("Enter two numbers separated with space:").split())
            res=DIV(a,b)
            print(f"Division of {a} and {b}:{res}")
        elif choice==5:
            print("Thanks for using the small calculator app")
            exit()    
        else:
            print("Invalid Choice")
