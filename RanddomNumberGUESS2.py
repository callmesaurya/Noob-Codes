import random                                # random module to randomize the SECRET NUMBER

lower = int(input('Enter Lower Range....'))  # Range in which USER wants to play
upper = int(input('Enter Upper Range....'))
random_number = random.randint(lower,upper)  # SECRET NUMBER chosen by COMPUTER... Each time different number is chosen
guess = 0                                    # TO Define the 'guess'
guess_count = 0                              # To keep track of 'Times taken to guess Correctly'

while guess != random_number:                # while guess in not equal to random number 

    guess = int(input(f'Choose a number between {lower} and {upper}: '))
    
    guess_count = guess_count+1              # adding 1 to guess count each time you make a guess

    if guess > random_number:
        print('Too High')

    elif guess < random_number:
        print('Too Low')

print(f'You guessed correctly..The number was {guess}')
print(f'You took {guess_count} guessses')

