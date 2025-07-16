#This is used to create a txt file in python,we can also add text or lists in txt files

employees = ["Saish","Anuj","Mahesh","Yash","Manthan"]

file_path = 'C:/Users/SAISH/OneDrive/output.txt'

try:
    with open('output.txt', 'w') as file:
        for employee in employees:
            file.write(employee +" ")
            print(f"txt file '{file_path}' was created")

except FileExistsError:
    print("This File is already created!")
