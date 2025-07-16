#Here we are writing or creating a json format file in python and will enter dictionary like data in it.

import json

employee = {
    "name": "Saish",
    "age": 20,
    "job": "SDE Intern",
    "skill": "Python",
}

file_path = ("C:/Users/SAISH/OneDrive/Desktop/output.json")

try:
    with open("output.json",'w') as file:
        for employees in employee:
            json.dump(employee,file,indent=4)
            print(f"json file {file_path} was created!")

except FileExistsError:
    print("This File already exists!")