#TRY-EXCEPT IS THE METHOD TO HANDLE ERRORS IN A PROGRAM.
# IT IS USED TO PRINT THE ERROR AND RUNS THE OTHER LINES OF CODE
#DUE TO THIS WE CAN HANDLE ERROR WITHOUT STOPPING THE CODE OR PROGRAM.
#SO LET'S TAKE AN EXAMPLE IN ORDER TO UNDERSTAND IT
a = input("Enter the number: ")
print(f"Multiplication Table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("This is the imp line of code")
print("End of program!")