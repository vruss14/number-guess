import random

# This function takes the user's guess, the computer's selection, and passes them both to check_guess

def ask_guess():
    user_guess = input('\nAwesome! I\'m thinking of a number between 1–10. What do you think it is?').lstrip().rstrip()
    cpu_choice = choose_number()
    check_guess(user_guess, cpu_choice)

# This function welcomes the user and prompts them to start the game

def print_intro():
    intro = input('\nWelcome to the game! Here\'s how this is going to work: You or I will guess a number from 1–10 and then the other will guess. Sound good? Just type "yes" or "no" to continue!').lower().lstrip().rstrip()

    if intro == 'yes':
        ask_guess()
    elif intro == 'no':
        print('\nNo worries! Hope I see you again soon!')
    else:
        print('\nI didn\'t understand what you meant. Please respond with "yes" or "no" next time.')

# Uses the random library to choose a random integer between 1 and 10; returns the number

def choose_number():
    chosen_number = random.randint(1, 10)
    return chosen_number

# Checks if the user's input was numeric and within the right range; then checks if the user and cpu values match

def check_guess(user, cpu):
    if(not user.isnumeric()):
        print('\nThat wasn\'t even a number!')
        subsequent_guess(cpu)
    elif( (int(user) > 10) or (int(user) < 1) ):
        print('\nThat\'s not between 1–10, silly!')
        subsequent_guess(cpu)
    elif(int(user) == int(cpu)):
        print(f'\nAw man! You got it! My number was {cpu}!')
        run_user_turn()
    else:
        subsequent_guess(cpu)

# Gives the user another guess if the user and cpu values don't match (i.e. the user guessed incorrectly)

def subsequent_guess(cpu):
    extra_guess = input('\nHaha! That\'s not it! Guess again!').lstrip().rstrip()
    check_guess(extra_guess, cpu)

# Runs the user turn prompt then calls the comp_guess with a full list from 1–10

def run_user_turn():
    your_turn = input('\nAll right, your turn! Think of a number between 1–10 and tell me when you\'ve got it. Just type "ready" when you have a number.').lower().lstrip().rstrip()
    number_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if(your_turn == 'ready'):
        comp_guess(number_options)
    else:
        print('\nSorry, I didn\'t understand you.')

# Accepts the list from the above function; uses that to try and make a random guess
# The try/except block makes sure that the numbers list is not empty (that would mean all the numbers were guessed)
# The user tells the computer if it guessed right; if not, then the computer will remove its previous guess 
# from the numbers list to avoid duplicate guesses, then run comp_guess again (with that modified list)

def comp_guess(numbers):

    try:
        cpu_guess = random.choice(numbers)
    except:
        print('\nWhat?! I guessed all the numbers between 1 and 10! That isn\'t fair!')
        return

    user_feedback = input(f'\nOkay I\'ve got it! Is your number {cpu_guess}? Just type "yes" or "no".').lower().lstrip().rstrip()

    if(user_feedback == 'yes'):
        play_again = input('\nYESSS!! Victory is so sweet! At least from what I\'ve heard... I\'m a computer so I don\'t actually taste things. But anyway, that was a lot of fun! Do you want to play again? Just type "yes" or "no".').lower().lstrip().rstrip()
        if(play_again == 'yes'):
            ask_guess()
        else:
            print('\nNo worries! That was a blast. Thanks for hanging out with me.')
    else:
        numbers.remove(cpu_guess)
        comp_guess(numbers)

print_intro()
    