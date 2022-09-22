# using string input comparison

from random import randint

print("lets play a game of")
print("Rock-Paper-Scissor")
print("Please Enter your Choice as :")
print("Rock")
print("Paper")
print("Scissors")

game = ['Rock','Paper','Scissors']

player_input = input("Enter your choice\n:")
random_input = randint(0,2)
computer_input = game[random_input]

print(f'computer',computer_input)

if player_input == computer_input:
    print("Its a TIE!")
elif player_input == 'Rock' and computer_input == 'Paper':
	print("computer wins")
elif player_input == 'Paper' and computer_input == 'Scissors':
   	print("computer wins")
elif player_input == 'Scissors' and computer_input == 'Rock':
   	print("computer wins")
else:
	print("player wins")
        
