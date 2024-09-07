# generate a number 1 - 10
import random
import sys


def playGame(guess, num):
    try:
        guess = int(guess)
        if 0 < guess < 11:
            if guess == num:
                print('You guessed it correct!')
                return True
        else:
            print('try again')
            return False
    except ValueError:
        print('Invalid input: enter a valid number')
        return False


if __name__ == '__main__':
    num = random.randint(1, 10)
    while True:
        try:
            guess = int(input('Enter your guess 1~10: '))
            if (playGame(guess, num)):
                break
        except ValueError:
            print('Please enter numbers')
            continue
