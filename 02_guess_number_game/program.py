import random

print('---------------------------------------')
print('       GUESS THAT NUMBER GAME')
print('---------------------------------------\n')


def game(a, b):
    the_number = random.randint(a, b)
    attempts = 0
    guess = a - 10

    while guess != the_number:

        guess_text = input('Guess a number between {0} and {1}: '.format(a, b))
        guess = int(guess_text)

        attempts += 1

        if guess < the_number:
            print('too low')
        elif guess > the_number:
            print('too high')
        else:
            print('You win! Number: {0}, Attempts: {1}\n'.format(the_number, attempts))


if __name__ == "__main__":

    while True:
        game(0, 100)

        if input('Do you want to keep playing? [Y]es / [Anything else -> No]').lower() != 'y':
            break
