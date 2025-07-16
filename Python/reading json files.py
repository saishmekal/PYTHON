import json
from json import JSONDecodeError

file_path = "C:/Users/SAISH/OneDrive/Desktop/Python/output.json"

try:
    with open(file_path,"r") as file:
        content = json.load(file)

        print(content["name"])

except JSONDecodeError:
    print("This file cant be decoded!")

#In this code i dont know why its showing error,but the format or syntax to read a json file is correct.ig there is a problem in my json file which i try to import
#we can also add other except errors to handle the errors like permissionerror which tells you that permission is denied to access this file.
# Filenotfound exception to put an error if the .format is not correctly typed or the type of file has not been created