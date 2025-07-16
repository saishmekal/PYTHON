#Here we are writing or creating a csv (comma separated files)format file in python and will enter dictionary like data in it.

import json
import csv

employee = [["name","age","job","hobby"],
            ["Saish",20,"SDE Intern","Football"],
            ["Anuj",20,"BMS Intern","Driving"],
            ["Mahesh",19,"BAF Intern","Football"]]


file_path = ("C:/Users/SAISH/OneDrive/Desktop/output.csv")

try:
    with open("output.csv",'w') as file:
        writer =csv.writer(file)
        for row in employee:
            writer.writerow(row)                      #method to write a row that is iterating for csv files!
            print(f"csv file {file_path} was created!")

except FileExistsError:
    print("This File already exists!")