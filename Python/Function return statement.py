#Returning a function for numbers
def add_numbers (num1,num2):

    result = num1 + num2
    return result

Sum = add_numbers(17,3)
print("The sum of two numbers is :" ,Sum)

#Returning a function for string
def Upper_string(str1,str2):

    result = str1 + str2
    return result.upper()

Capital_string = Upper_string("saish", "mekal")
print("The sum of two strings is:",Capital_string)