import random

computer_turn = random.choice(['r','p','s'])   # Computer have to something from R-P-S

user_turn = input('Choose from R for Rock, P for Paper, S for Scissor: ')

if user_turn=='r' and computer_turn=='s':
    print('User Won')
    print(f'Computer choose:{computer_turn},You Choose: {user_turn}')
elif user_turn=='p' and computer_turn=='r':
    print('User Won')
    print(f'Computer choose:{computer_turn},You Choose: {user_turn}')
elif user_turn=='p' and computer_turn=='s':
    print('Computer Won')
    print(f'Computer choose:{computer_turn},You Choose: {user_turn}')
elif user_turn=='s' and computer_turn=='r':
    print('Computer Won')
    print(f'Computer choose:{computer_turn},You Choose: {user_turn}')
elif user_turn=='r' and computer_turn=='p':
    print('User Won')
    print(f'Computer choose:{computer_turn},You Choose: {user_turn}')
elif user_turn=='s' and computer_turn=='p':
    print('Computer Won')
    print(f'Computer choose:{computer_turn},You Choose: {user_turn}')
elif user_turn == computer_turn:
    print('Match Drawn')