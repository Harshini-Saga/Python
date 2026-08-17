#add 1 to n numbers in output.txt file
file=None
try:
    file=open("output.txt","w")
    n=5
    for i in range(1,n+1):
        file.write(str(i)+"\n")
except Exception as e:
    print(f"Something wrong:{e}")
finally:
    if file:
        file.close()