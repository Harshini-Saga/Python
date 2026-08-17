#opening a file in write mode
# file=open("sample.txt","w")
# file.write("I am Harshini")
# file.close()
# print("Contents Added")

# #opening a file in append mode
# file=open("sample.txt","a")
# file.write("I am Harshini")
# file.close()
# print("Contents Added")

#add content at start of the file and open in append mode
#opening a file in append mode
# file=open("sample1.txt","r")
# string="""I am a student
# I am learning Python"""
# file.seek(0)
# file.write(string)
# file.close()
# print("Contents Added")

##Opening a file in read mode
file=None
try:
    file=open("sample.txt","r")
    data=file.readlines()
    print(data)
except Exception as e:
    print(f"Something Wrong, because: {e}")
finally:
    if file:
        file.close()