import random

def ask_guess():
    user_guess = input('Awesome! I\'m thinking of a number between 1–10. What do you think it is?').lstrip().rstrip()
    cpu_choice = choose_number()
    check_guess(user_guess, cpu_choice)

def print_intro():
    intro = input('Welcome to the game! Here\'s how this is going to work: You or I will guess a number from 1–10 and then the other will guess. Sound good? Just say yes or no to continue!').lower().lstrip().rstrip()

    if intro == 'yes':
        ask_guess()
    elif intro == 'no':
        print('No worries! Hope I see you again soon!')
    else:
        print('I didn\'t understand what you meant. Please respond with yes or no next time.')

def choose_number():
    chosen_number = random.randint(1, 10)
    return chosen_number

def check_guess(user, cpu):
    if(int(user) == int(cpu)):
        print('You got it on your FIRST try?!? You must be a mind reader! Way to go!')
        run_user_turn()
    else:
        subsequent_guess(cpu)

def subsequent_guess(cpu):
    extra_guess = input('Haha! That\'s not it! Guess again!').lstrip().rstrip()
    if(int(extra_guess) == int(cpu)):
        print(f'Aw man! You got it! My number was {cpu}!')
        run_user_turn()
    else:
        subsequent_guess(cpu)

def run_user_turn():
    your_turn = input('All right, your turn! Think of a number between 1–10 and tell me when you\'ve got it. Just say "ready" when you have a number.').lower().lstrip().rstrip()
    number_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if(your_turn == 'ready'):
        comp_guess(number_options)
    else:
        print('Sorry, I didn\'t understand you.')

def comp_guess(numbers):
    print(numbers)
    cpu_guess = random.choice(numbers)
    user_feedback = input(f'Okay I\'ve got it! Is your number {cpu_guess}? Just say yes or no.').lower().lstrip().rstrip()

    if(user_feedback == 'yes'):
        play_again = input('YESSS!! Victory is so sweet! At least from what I\'ve heard... I\'m a computer so I don\'t actually taste things. But anyway, that was a lot of fun! Do you want to play again? Just say yes or no.')
        if(play_again == 'yes'):
            ask_guess()
        else:
            print('No worries! That was a blast. Thanks for hanging out with me.')
    else:
        numbers.remove(cpu_guess)
        comp_guess(numbers)

print_intro()
    