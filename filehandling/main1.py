# import csv
# try:
#     with open("test.csv","w",newline="") as file:
#         writer = csv.writer(file)
#         header = ['Name','contact']
#         writer.writerow(header)
#         data=[['ram',987654321],['sam',912345678]]
#         writer.writerows(data)
#         print("Contents added")
# except Exception as e:
#     print(f"Something wrong: {e}")

#Reading a csv file
# import csv
# try:
#     with open("test.csv","r",newline="") as file:
#         reader = csv.reader(file)
#         #print(list(reader))
#         for row in reader:
#             print(row)
#         print("Contents added")
# except Exception as e:
#     print(f"Something wrong: {e}")

## Updating contact number
# import csv
# try:
#     with open("test.csv","r",newline="") as file:
#         reader = csv.reader(file)
#         contacts=list(reader)
#         name=input()
#         new_contact=input()
#         for ind,row in enumerate(contacts):
#             if row[0]==name:
#                 contacts[ind][1]=new_contact
#                 break
#         else:
#             print("Contact name does not exists")
# except Exception as e:
#     print(f"Something wrong: {e}")\

# ##writing content into file
# try:
#     with open("test.csv","w",newline="") as file:
#         writer = csv.writer(file)
#         writer.writerows(contacts)
#         print("Contents added")
# except Exception as e:
#     print(f"Something wrong: {e}")

#Add contact to the file
import csv
try:
    with open("test.csv","r",newline="")as file:
        reader=csv.reader(file)
        contacts=list(reader)
        name=input()
        number=input()
        for row in contacts:
            if row[0]==name:
                print("Name already exists")
                break
            elif row[1]==number:
                print("Number already exists")
                break
        else:
            contacts.append([name,number])
except Exception as e:
    print(f"Something wrong: {e}")
#writing content into file
try:
    with open("test.csv","w",newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)
        print("Contact added Successfully")
except Exception as e:
    print(f"Something wrong: {e}")
