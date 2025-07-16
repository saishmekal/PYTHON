#IN THIS PROGRAM WE HAVE USED ValueError as a raising exceptions
#AND WE HAVE USED TRY AND EXCEPT CONCEPT TO PRINT THE ERROR AND RUN THE REMAINING CODE FOR EXECUTION WITHOUT INTERRUPTING


a = int(input("Enter any number between 5 and 9: "))

try:
    if (a<5 or a>9):
        raise ValueError("Invalid Number,try to enter between 5 and 9")

except ValueError as e:
    print(e)