# generate a number 1 - 10
import random

num = random.randint(0, 10)
# input from user for the guess

# check the input is a number

# check if  number is the right guess. Otherwise
while True:
    try:
        guess = int(input('Enter your guess 1~10: '))
        if 0 < guess < 11 and guess == num:
            print('You guessed it correct!')
            break
        else:
            print('try again')
            continue
    except ValueError:
        print('Please enter numbers')

# ask again
