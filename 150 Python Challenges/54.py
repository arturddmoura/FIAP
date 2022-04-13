#Randomly choose either heads or tails (“h” or “t”). Ask the user to make their choice. If their choice is the same as the randomly selected value, display the message “You win”, otherwise display “Bad luck”. At the end, tell the user if the computer selected heads or tails.
import random

computer = random.choice(['heads', 'tails'])
player = input('Please select heads or tails: ')

if player.upper() == computer.upper():
    print('You win! ')

else:
    print('Better luck next time! ')

print(f'The computer selected {computer}. ')