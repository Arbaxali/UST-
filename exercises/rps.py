# player1 = input("enter the player name ")
# player2 = input("enter the player name ")


# choice1 = input("Choose rock,paper,scissor ").lower()
# choice2  =input("Choose rock,paper,scissor ").lower()


# if choice1 == choice2 :
#     print("DRAW")
# elif choice1 == "rock" and choice2 == "scissor":
#     print("{0} wins ".format(player1))
# elif choice1 == "rock" and choice2 == " paper":
#     print("hekk")
#     print("{0} wins".format(player2))    
# elif choice1 == "scissor" and choice2 == " paper":
#     print("{0} wins".format(player1))   


from tkinter.messagebox import NO


while True:
    choices = ["rock","paper","scissors"]

    player1 = None
    player2 = None

    while player1 not in choices:
        player1 = input("player1 :rock, paper, or scissors?: ").lower()
    while player2 not in choices:
        player2 = input("player2: rock, paper, or scissors?: ").lower()

    if player1 == player2:
        print("########################")
        print("player2: ",player2)
        print("player1: ",player1)
        print("Tie!")
        print("########################")

    elif player1 == "rock":
        if  player2 == "paper":
            print("########################")
            print("player2: ", player2)
            print("player1: ", player1)
            print("player1 lose!")
            print("player2 win!")
            print("########################")
        if player2 == "scissors":
            print("########################")
            print("player2: ", player2)
            print("player1: ", player1)
            print("player1 win!")
            print("player2 lose!")
            print("########################")

    elif player1 == "scissors":
        if player2 == "rock":
            print("########################")
            print("player2: ",player2)
            print("player1: ", player1)
            print("player1 lose!")
            print("player2 win!")
            print("########################")
        if player2 == "paper":
            print("########################")
            print("player2: ", player2)
            print("player1: ", player1)
            print("player1 win!")
            print("player2 lose!")
            print("########################")

    elif player1 == "paper":
        if player2 == "scissors":
            print("########################")
            print("player2: ", player2)
            print("player1: ", player1)
            print("player1 lose!")
            print("player2 win!")
            print("########################")
        if player2 == "rock":
            print("########################")
            print("player2: ", player2)
            print("player1: ", player1)
            print("player1 win!")
            print("player2 lose!")
            print("########################")
