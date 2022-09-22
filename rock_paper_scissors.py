# using Flask to create a server run code  
# Flask is the framework which acts as a central hub between frontend and backend

from flask import Flask, render_template
from random import randint

app = Flask('rock paper scissors')

options = ['rock','paper','scissors','lizard','spock']

def computer_basic_game():
    computer_basic_choise = options[randint(0,2)]
    return computer_basic_choise

def computer_tbbt_game():
    computer_tbbt_choise = options[randint(0,4)]
    return computer_tbbt_choise

def run_game(computer_selection,player_selection):
    if computer_selection == player_selection:
        winner = 'tie'
    elif computer_selection == 'scissors' and player_selection == 'paper':
        winner = 'computer'
    elif computer_selection == 'scissors' and player_selection == 'lizard':
        winner = 'computer'
    elif computer_selection == 'paper' and player_selection == 'rock':
        winner = 'computer'
    elif computer_selection == 'paper' and player_selection == 'spock':
        winner = 'computer'
    elif computer_selection == 'rock' and player_selection == 'scissors':
        winner = 'computer'
    elif computer_selection == 'rock' and player_selection == 'lizard':
        winner = 'computer'
    elif computer_selection == 'lizard' and player_selection == 'spock':
        winner = 'computer'
    elif computer_selection == 'lizard' and player_selection == 'paper':
        winner = 'computer'
    elif computer_selection == 'spock' and player_selection == 'scissors':
        winner = 'computer'
    elif computer_selection == 'spock' and player_selection == 'rock':
        winner = 'computer'
    else:
        winner = 'player'

    print(winner)

    return winner

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/basic')
def basic():
    return render_template('basic.html')

@app.route('/tbbt')
def tbbt():
    return render_template('tbbt.html')

@app.route('/basic_game/<player_selection>')
def basic_game(player_selection):
    computer = computer_basic_game()
    player = player_selection
    winner = run_game(computer,player)
    print(player_selection)
    print(computer)
    print(winner)
    return render_template('basic_result.html',winner = winner, computer = computer, player = player)

@app.route('/tbbt_game/<player_selection>')
def tbbt_game(player_selection):
    computer = computer_tbbt_game()
    player = player_selection
    winner = run_game(computer,player)
    print(player_selection)
    print(computer)
    print(winner)
    return render_template('tbbt_result.html',winner = winner, computer = computer, player = player)




app.run(port=8888)
