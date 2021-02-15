#user imports random function from which computer can playe random moves
from random import randint
#initialising the variables
player_wins = 0
computer_wins = 0
winning_score = 3
#for checking both variables reaches to winning score
while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player score:{player_wins} | Computer Scores:{computer_wins}")
    print("...Rock...")
    print("...Paper...")
    print("...Scissors...")
    
    rand_num = randint(0,2)#create a variable from which computer can initailise the main variables i.e. rock, paper, scissor
    # user will enter the data which will converted to lower case with help of lower function and stores it to variable name 'player'
    player = input("Enter the move:\n").lower()
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"Computer plays {computer}")
    # the conditions of the game
    if player == computer:
        print("its a Tie")
    elif player == "rock":
        if computer == "scissor":
            print("PLayer Wins")
            player_wins += 1
        elif computer == "paper":
            print("Computer Wins")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player Wins")
            player_wins += 1
        elif computer == "scissor":
            print("Computer Wins")
            computer_wins += 1
    elif player == "scissor":
        if computer == "paper":
            print("Player Wins")
            player_wins += 1
        elif computer == "rock":
            print("Computer Wins")
            computer_wins += 1
    else:
        print("Please enter valid move")
    # conditions who wins the game
    if player_wins > computer_wins:
        print("Congrats! You Win")
    elif player_wins == computer_wins:
        print("It's a Tie Bracker")
    else:
        print("Computer Wins the game")
    #end