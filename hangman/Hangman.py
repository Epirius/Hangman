import random
from Hangman_List import word_list


def word_picker():
    answer = word_list[random.randint(0, len(word_list) - 1)]
    return answer


def player_guess(current_guess, answer):
    print('the current guess is:  ' + "".join(current_guess))

    while True:
        guess = input('pick a letter: ')
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('invalid input')
    guess = guess.lower()

    if answer.find(guess) == -1:  # the guess was wrong
        # TODO: punish worng guess and ask for new guess
        print('wrong guess')
    else:		# The guess was right
        for i in range(len(answer)):
            if answer[i] == guess:
                current_guess[i] = guess
        print('you guessed correctly!')
        print("\n" * 2)
        return current_guess


def main():
    answer = word_picker()
    current_guess = list('-' * len(answer))
    print(answer)  # TODO: TEMP, DELETE THIS LINE
    print('The word i am thinking of is %s letters long' % len(answer))
    while '-' in current_guess:
        player_guess(current_guess, answer)
    if '-' not in current_guess:
        print("".join(current_guess))
        print('You Won!')


main()
