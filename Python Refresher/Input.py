# The input function always gives you a string

name = input("Enter your name:\n")

# Type casting string input to a number
number = int(input("Enter a number:\n"))

print("{} {} {} {}".format(name,number,type(name),type(number)))

