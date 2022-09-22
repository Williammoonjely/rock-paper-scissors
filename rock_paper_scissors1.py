#using intiger input

from random import randint
import os

print("Lets play a game of 'Rock-Paper-Scissor'")
choice = ['','Rock','Paper','Scissors']
count = 0
computer_count = 0
player_count = 0
tie_count = 0
play_again = 'go'
high_score = int(input("Enter the high score at which game ends :"))

while play_again != 'x':

    print("Please Enter '1' for Rock '2' for Paper '3' for Scissors 'x' to exit")
    user_input = input('Enter your choice :\n')
    computer_input = randint(1,3)

    valid = 'false'
    while valid != 'True':
        if user_input == '1' or user_input == '2' or user_input == '3' or user_input == 'x':
            valid = 'True'
        else:
            user_input = input('Enter a valid choice :\n')

    if user_input != 'x':
        player_input = int(user_input)    
        

        if player_input == computer_input:
            os.system('clear')
            print(f"Player choice: '{choice[player_input]}' Computer choice: '{choice[computer_input]}'")
            print("Its a TIE!")
            tie_count += 1
            count += 1
        elif player_input < computer_input:
            os.system('clear')
            print(f"Player choice: '{choice[player_input]}' Computer choice: '{choice[computer_input]}'")
            print("Computer WINS!")
            computer_count += 1
            count += 1
        elif player_input == 3 and computer_input == 1:
            os.system('clear')
            print(f"Player choice: '{choice[player_input]}' Computer choice: '{choice[computer_input]}'")
            print("Computer WINS!")
            computer_count += 1
            count += 1
        else:
            os.system('clear')
            print(f"Player choice: '{choice[player_input]}' Computer choice: '{choice[computer_input]}'")
            print("Player WINS!")
            player_count += 1
            count += 1   
    else:
        os.system('clear')
        play_again = 'x'
        print("Player exited before game ended")

    
    print(f"Player : {player_count} Computer : {computer_count} Ties:{tie_count}")
    print(f"the no games:{count}")
    

    if player_count == high_score:
        play_again = 'x'
        print("The ultimate winner is computer")
    elif computer_count == high_score:
        play_again = 'x'
        print("The ultimate winner is player")
    else:
        pass
    
