#using function


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
os.system('clear')
print("Player choice: 'None' Computer choice: 'None' \nLets Begin The Game")
print(f"Player : {player_count} Computer : {computer_count} Ties:{tie_count}")
def rps(choice,count,computer_count,player_count,tie_count,play_again,high_score):

    if player_count < high_score and computer_count < high_score:

        print("Please Enter '1' for Rock '2' for Paper '3' for Scissors 'x' to exit")
        user_input = input('Enter your choice :\n')
        computer_input = randint(1,3)
        valid = 'false'
        
        while valid != 'True':
            if user_input == '1' or user_input == '2' or user_input == '3':
                player_input = int(user_input)
                valid = 'True'

                if player_input == computer_input:
                    os.system('clear')
                    tie_count += 1
                    count += 1
                    print(f"Player choice: '{choice[player_input]}' Computer choice: '{choice[computer_input]}'")
                    print("Its a TIE!")
                    print(f"Player : {player_count} Computer : {computer_count} Ties:{tie_count}")
                    rps(choice,count,computer_count,player_count,tie_count,play_again,high_score)
                elif player_input < computer_input:
                    os.system('clear')
                    computer_count += 1
                    count += 1
                    print(f"Player choice: '{choice[player_input]}' Computer choice: '{choice[computer_input]}'")
                    print("Computer WINS!")
                    print(f"Player : {player_count} Computer : {computer_count} Ties:{tie_count}")
                    rps(choice,count,computer_count,player_count,tie_count,play_again,high_score)
                elif player_input == 3 and computer_input == 1:
                    os.system('clear')           
                    computer_count += 1
                    count += 1
                    print(f"Player choice: '{choice[player_input]}' Computer choice: '{choice[computer_input]}'")
                    print("Computer WINS!")
                    print(f"Player : {player_count} Computer : {computer_count} Ties:{tie_count}")
                    rps(choice,count,computer_count,player_count,tie_count,play_again,high_score)
                else:
                    os.system('clear')
                    player_count += 1
                    count += 1
                    print(f"Player choice: '{choice[player_input]}' Computer choice: '{choice[computer_input]}'")
                    print("Player WINS!")
                    print(f"Player : {player_count} Computer : {computer_count} Ties:{tie_count}")  
                    rps(choice,count,computer_count,player_count,tie_count,play_again,high_score) 
            elif user_input == 'x':
                valid = 'True'
                os.system('clear')       
                print(f"Player : {player_count} Computer : {computer_count} Ties:{tie_count}")
                print(f"the no games:{count}")
                print("Player exited before game ended")
            else:
                user_input = input('Enter a valid choice :\n')
    elif player_count == high_score:
        print(f"the no games:{count}")
        print("The ultimate winner is Player")
    elif computer_count == high_score:
        print(f"the no games:{count}")
        print("The ultimate winner is Computer")
    else:
        pass
    
rps(choice,count,computer_count,player_count,tie_count,play_again,high_score)
