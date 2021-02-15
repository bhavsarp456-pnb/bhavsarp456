from random import randint
player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print("...Rock...")
    print("...Paper...")
    print("...Scissors...")
    print(f"Player Score:{player_wins}|"f"Computer Score:{computer_wins}")

    rand_num = randint(0,2)
    player = input("Enter your move:").lower()
    if rand_num == 0:
        computer = "Rock"
    elif rand_num == 1:
        computer = "Paper"
    else:
        computer = "Scissors"
    
    if player == computer:
        print("Its a Tie.")
        print(f"Computer plays:{computer}")
    elif player == "rock":
        if computer == "scissors":
            print("Player Wins")
            player_wins += 1
        elif computer == "paper":
            print("computer Wins")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player Wins")
            player_wins += 1
        elif computer == "scissors":
            print("Computer Wins")
            computer_wins += 1
    elif player == "scissors":
        if computer == "Paper":
            print("Player Wins")
            player_wins += 1
        elif computer == "Rock":
            print("Computer Wins")
            computer_wins += 1
    else:
        print("Please Enter your valid move.....")
    
    if player_wins > computer_wins:
        print("Congrats! You Won....")
    elif player_wins == computer_wins:
        print("Its Tie Breaker....")
    else:
        print("Computer Wins Better luck next time")
