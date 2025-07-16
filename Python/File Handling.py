#File handling in python is used to read,write or add any data or text within the file
#It can be used as a temporary database where we can read,write and edit files
#There are many ways to handle files,and they are as follows:

#1.read()
f= open('basic.py','r')  #'open()' is used to open any existing file
text = f.read()
print(text)
f.close()


#2.write()
f = open('blank.py', 'w') #'write()' is used to write any text on the file but it doesn't save the data on that file
file= f.write("Hello This is a blank doc for testing!") #Here the file wasn't created at first but in write command it automatically creates file if it isn't!
print(file)
f.close()

#3.append()
f = open('blank.py', 'a') #'append()' is used to add text to the file and it also saves the added data to the file!
app=f.write("This text is create to append this text on the blank.py file!") #In this case the append() saves the added text for further reference
print(app)
f.close()

#Another way to write,read or append files is by using 'with' command!

with open('blank.py', 'r') as f: #Basically 'with' operation is another way to write the file handling method,you can perform read(),write() and append() on these too!
    reading = f.read()
    print(reading)  #Here we don't have to add close operation like other methods!