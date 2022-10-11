# snake gun  water game in python

while True:
    choices = ["snake","gun","water"]

    player1 = None
    player2 = None

    while player1 not in choices:
        player1 = input("player1 :snake ,gun or water ").lower()
    while player2 not in choices:
        player2 = input("player2: snake ,gun or water ").lower()
    
    # if player1 not in choices and player2 not in choices:
    #     print("select from given option")
    #     break
            


    if player1 == player2:
        print("########################")
        print("player2: ",player2)
        print("player1: ",player1)
        print("Tie!")
        print("########################")

    elif player1 == "snake":
        if  player2 == "water":
            print("########################")
            print("player2: ", player2)
            print("player1: ", player1)
            print("player1 win!")
            print("player2 loose!")
            print("########################")
        if player2 == "gun":
            print("########################")
            print("player2: ", player2)
            print("player1: ", player1)
            print("player1 loose!")
            print("player2 win!")
            print("########################")
    elif player1 == "gun":
        if player2 == "water":
            print("########################")
            print("player2: ",player2)
            print("player1: ", player1)
            print("player1 lose!")
            print("player2 win!")
            print("########################")
        if player2 == "snake":
            print("########################")
            print("player2: ", player2)
            print("player1: ", player1)
            print("player1 win!")
            print("player2 lose!")
            print("########################")
    elif player1 == "water":
        if player2 == "snake":
            print("########################")
            print("player2: ", player2)
            print("player1: ", player1)
            print("player1 lose!")
            print("player2 win!")
            print("########################")
        if player2 == "gun":
            print("########################")
            print("player2: ", player2)
            print("player1: ", player1)
            print("player1 win!")
            print("player2 lose!")
            print("########################")
