print("...Rock...")
print("...Paper...")
print("...SCissor...")
 
Player1 = input("Please enter your move:")
Player2 = input("Please enter your move:")

if (
     (Player1 == "Rock" and Player2 == "Scissor")
     or (Player1 == "Paper" and Player2 == "Rock")
     or (Player1 == "Scissor" and Player2 == "Paper")
    ):
    print("Player1 Wins")

elif (
    (Player2 == "Rock" and Player1 == "Scissor")
     or (Player2 == "Paper" and Player1 == "Rock")
     or (Player2 == "Scissor" and Player1 == "Paper")
    ):
    print("Player2 Wins")

elif (
    (Player1 == Player2)
    ):
    print("It's a Tie")

else:
    print("Something went wrong.")
    