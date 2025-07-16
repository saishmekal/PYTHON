print("WELCOME TO THE BEAST ATM!")

balance = 1000

password = "1234"

try_pass = input("Please enter your pin to proceed: ")
if try_pass != password:
    print("Incorrect Pin,Exiting:")
    atm_on = False
else:
    print("You,ve Successfully Logged In!")
    atm_on = True

while atm_on:
    print("Main Menu")
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.EXIT")

    choice = input("Enter Your Choice: ")
    if choice == "1":
        print("Your Current Balance is $" + str(balance))

    elif choice == "2":
        amount = float(input("Enter the amount to deposit: $"))
        balance = balance + amount
        print("Your new Balance after depositing is $" +str(balance))

    elif choice == "3":
        amount = float(input("Enter the amount to be withdrawn: "))
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance = balance - amount
            print("Your Balance after withdrawal is $" +str(balance))

    elif choice == "4":
        print("Thank you for using the BEAST ATM!")
        atm_on = False

    else:
        print("Invalid choice,Please try again.")