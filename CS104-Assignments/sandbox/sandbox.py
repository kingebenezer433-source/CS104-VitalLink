number = input("Enter an integer: ")

try:
    number = int(number)
except:
    print("That's not a valid integer. Please try again.")
    exit()

print("Your number:", number)