import random

computer_number = random.randrange(1,101)

user_input = int(input('Enter your numer :'))

if user_input > computer_number:
    print('computer_number is:',computer_number)
    print('Your number is greter than computer_number')
elif user_input < computer_number:
    print("computer number is :",computer_number)
    print("Your number is less than computer_number")
else:
    print("computer number is :",computer_number)
    print('Your number is equal to the computer_number')


