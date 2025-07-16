count = 1
while count <=5:
    print(count)

    user_in = input("Enter 'exit' to end")
    if user_in.lower() == ('exit'):
        print("You are terminating the code.")
        break

    count = count + 1
