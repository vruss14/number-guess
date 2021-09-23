import random

intro = input('Welcome to the game! Here\'s how this is going to work: You or I will guess a number from 1–10 and then the other will guess. Sound good? Just say yes or no to continue!').lower().lstrip().rstrip()
print(intro)

def choose_number():
    chosen_number = random.randint(1, 10)
    print(chosen_number)


if intro == 'yes':
    input('Awesome! I\'ll go first. I\'m thinking of a number between 1–10. What do you think it is?')
    choose_number()
elif intro == 'no':
    print('No worries! Hope I see you again soon!')
else:
    print('I didn\'t understand what you meant. Please respond with yes or no next time.')


    