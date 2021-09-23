import random
intro = input('Welcome to the game! Here\'s how this is going to work: You or I will guess a number from 1–10 and then the other will guess. Sound good? Just say yes or no to continue!').lower().lstrip().rstrip()

def choose_number():
    chosen_number = random.randint(1, 10)
    return chosen_number

def ask_guess():
    user_guess = input('Awesome! I\'ll go first. I\'m thinking of a number between 1–10. What do you think it is?')
    cpu_choice = choose_number()
    check_guess(user_guess, cpu_choice)

def check_guess(user, cpu):
    print(user)
    print(cpu)
    if(int(user) == int(cpu)):
        print('Woohoo! That\'s right!')
    else:
        subsequent_guess(cpu)

def subsequent_guess(cpu):
    extra_guess = input('Haha! That\'s not it! Guess again!')
    if(int(extra_guess) == int(cpu)):
        print('Aw man! You got it!')
    else:
        subsequent_guess(cpu)

if intro == 'yes':
    ask_guess()
elif intro == 'no':
    print('No worries! Hope I see you again soon!')
else:
    print('I didn\'t understand what you meant. Please respond with yes or no next time.')


    