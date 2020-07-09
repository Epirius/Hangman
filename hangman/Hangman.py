import random
import os
import sys
from Hangman_List import word_list


wrong_guess = 0
wrong_letters = []
wrong_allowed = 5


def word_picker():
    answer = word_list[random.randint(0, len(word_list) - 1)]
    return answer


def player_guess(current_guess, answer):
    print('the current guess is:  ' + "".join(current_guess))
    global wrong_guess
    if wrong_guess >= wrong_allowed:
        end(current_guess, answer)

    while True:
        # input validation:
        guess = input('pick a letter: ')
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('invalid input')
    guess = guess.lower()
    global wrong_letters

    # right or wrong guess:
    if answer.find(guess) == -1:  # the guess was wrong
        if guess not in wrong_letters:
            wrong_letters = wrong_letters + list(guess)

        wrong_guess = wrong_guess + 1
        os.system('cls')
        print('wrong guess')
        print('You have %s wrong guesses: ' %
              wrong_guess + ", ".join(wrong_letters))

    else:		# The guess was right
        for i in range(len(answer)):
            if answer[i] == guess:
                current_guess[i] = guess
        os.system('cls')
        print('you guessed correctly!')
        print('You have %s wrong guesses: ' %
              wrong_guess + ", ".join(wrong_letters))
        return current_guess


def end(current_guess, answer):
    os.system('cls')
    print('Game over: you guessed to many times')
    print('Your guess was: ' + "".join(current_guess))
    print('The answer was: ' + answer)
    print()
    input('Press any key to end')
    sys.exit(0)


def main():
    answer = word_picker()
    current_guess = list('-' * len(answer))
    print('The word i am thinking of is %s letters long' % len(answer))
    while '-' in current_guess:
        player_guess(current_guess, answer)
    if '-' not in current_guess:
        os.system('cls')
        print("".join(current_guess))
        print('You Won!')
        print('You had %s wrong guesses' % wrong_guess)
        input('press any key to end')
        sys.exit(0)


main()
