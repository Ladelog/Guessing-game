import random
computer_guess = random.randint(1, 100)
user_guess = int(input("Guess a number: "))
if user_guess > computer_guess:
    print("Number is too big")
elif user_guess < computer_guess:
    print("Number is too low")
elif user_guess == computer_guess:
    print("You have tried more than expected, but you win! ")
else:
    print("Try again")
