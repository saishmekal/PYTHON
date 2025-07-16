import random
def computer_decision():
    choices = ["rock","paper","scissors"]
    return random.choice(choices)

def user_decision():
    user_choice = input("Enter rock,paper or scissors (or 'q' to end): ").lower()
    while user_choice not in ("rock","paper","scissors"):
        user_choice = input("Invalid Input!.Enter rock,paper,scissors (or 'q' to end): ").lower()
        return user_choice

def deciding_winner(user_choice2,computer_choice):
    if user_choice2 == computer_choice:
        print("It's a Tie!")

    elif (user_choice2 == "rock" and computer_choice == "scissors") or \
            (user_choice2 == "paper" and computer_choice == "rock") or \
            (user_choice2 == "scissors" and computer_choice == "paper"):
        return("You win!")

    else:
        return("Computer Won!")

def play_game():
    while True:
        user_choice2 = user_decision()
        if user_choice2 == 'q':
            print("Thanks for playing!")
            break

        computer_choice = computer_decision()
        print(f"You chose {user_choice2},Computer chose {computer_choice}!")

        result = deciding_winner(user_choice2,computer_choice)
        print(result)

play_game()



