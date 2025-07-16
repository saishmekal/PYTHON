import json
import csv

file_path = "C:/Users/SAISH/OneDrive/Desktop/Python/output.csv"
with open(file_path,'r') as file:
    content = csv.reader(file)
    for line in content:
        print(line[0])
    print(content)

#We can also add try except handling methods in this file for any such applicable errors!