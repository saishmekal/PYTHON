print("Give me two numbers I'll divide it")
print("Enter q to exit.")

while True:
    first_number =(input("Enter First number: "))
    if first_number == "q":
        break
    second_number =input("Enter second number: ")
    try:
        result = int(first_number) / int(second_number)
        print(result)
    except ZeroDivisionError:
        print("You can't divide by zero!")

    except ValueError:
        print("Use numerical values only!")