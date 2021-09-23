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
    else:
        subsequent_guess(cpu)

def subsequent_guess(cpu):
    extra_guess = input('Haha! That\'s not it! Guess again!').lstrip().rstrip()
    if(int(extra_guess) == int(cpu)):
        print(f'Aw man! You got it! My number was {cpu}!')
    else:
        subsequent_guess(cpu)

print_intro()
    