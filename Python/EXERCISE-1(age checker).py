# MY CODE FOR AGE VERIFICATION
user = input("Enter your age: ")
user = int(user)
if user < 18:
    print("You're too young for this ride.")
elif user > 45:
    print("You,re too old for this ride.")
else:
    print("Enjoy the ride!")


# INSTRUCTOR'S CODE FOR AGE VERIFICATION
print("To get the access of the ride!")
user_age = input("Enter your age: ")
user_age = int(user_age)
if user_age >= 18 and user_age <= 45:
    print("Enjoy the ride.")
elif user_age < 18:
    print("You're too young for this ride.")
elif user_age > 45:
    print("You're too old for this ride.")
