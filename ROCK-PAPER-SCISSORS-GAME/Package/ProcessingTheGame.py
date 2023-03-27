def ProcessingTheGame(choiceList,PlayerName):
    "Processing the game"
    #Creating and initializing the variables
    Score_Of_the_Computer=0
    Score_Of_the_HumanPlayer=0
    computer_wins=0
    HumanPlayer_wins=0
    Total_game_plays=0
    Total_draws = 0
    
    #importing random
    import random
    print("") #To get a clean output
    userChoice = input("Do you want to play ? (Yes/No): ")
    print("") #To get a clean output
    
    #Processing the game
    while (userChoice == "Yes"):
        #Getting the choice from the Computer
        Computer = random.choice(choiceList)
        Player2= input("Enter your choice here(Rock,Paper,Scissors): ")
        if (Computer==Player2):
            print("YOU and the Computer chose the same,Game TIED")
            Total_draws = Total_draws + 1 #Calculating the draw games
            Total_game_plays=Total_game_plays+1 #Calculating the total no. of games
            continue
        while (Player2 == "Scissors"):
            if (Computer == "Paper"):
                print("You chose Scissors and the Computer chose Paper, You WON!")
                Score_Of_the_HumanPlayer=Score_Of_the_HumanPlayer+1 #Score of the Human player
                HumanPlayer_wins=HumanPlayer_wins+1 #Wins by the Human player
                Total_game_plays=Total_game_plays+1 #Calculating the total no. of games
                
            elif (Computer == "Rock"):
                print("YOU chose Scissors and the Computer chose Rock, You LOSE!")
                Score_Of_the_Computer=Score_Of_the_Computer+1 #Score of the Computer
                computer_wins=computer_wins+1 #Wins by the Computer
                Total_game_plays=Total_game_plays+1 #Calculating the total no. of games
            break
        while (Player2 == "Paper"):
            if(Computer == "Scissors"):
                print("You chose Paper and the Computer chose Scissors, you Lose!")
                Score_Of_the_Computer=Score_Of_the_Computer+1 #Score of the Computer
                computer_wins=computer_wins+1 #Wins by the Computer
                Total_game_plays=Total_game_plays+1 #Calculating the total no. of games
            elif (Computer=="Rock"):
                print("You chose Paper and the Computer chose Rock You WON!")
                Score_Of_the_HumanPlayer=Score_Of_the_HumanPlayer+1 #Score of the Human player 
                HumanPlayer_wins=HumanPlayer_wins+1 #Wins by the Human player
                Total_game_plays=Total_game_plays+1 #Calculating the total no. of games
            break
        while (Player2=="Rock"):
            if (Computer=="Paper"):
                print("You chose Rock and the Computer chose Paper,YOU LOSE!")
                Score_Of_the_Computer=Score_Of_the_Computer+1 #Score of the Computer
                computer_wins=computer_wins+1 #Wins by the Computer
                Total_game_plays=Total_game_plays+1 #Calculating the total no. of games
            elif (Computer =="Scissors"):
                print("You chose Rock and the Computer chose Scissors! You WON!!")
                Score_Of_the_HumanPlayer=Score_Of_the_HumanPlayer+1 #Score of the Human player
                HumanPlayer_wins=HumanPlayer_wins+1 #Wins by the Human player
                Total_game_plays=Total_game_plays+1 #Calculating the total no. of games
            break
        print("")#A space is given to get a clear output
        print("Wins by the human: " +str (HumanPlayer_wins))#Converting to a string
        print("Wins by the computer: " +str (computer_wins))#Converting to a string
        print("Total number of draws: " +str( Total_draws)) # converting to a string
        print("Total Number of Games played:" +str(Total_game_plays))#Converting to a string
        userChoice=input("Do you want to play again? (Yes/No): ")#Asking the human player's choice on playing again
        print("")#A space is given to get a clear output
        
    while userChoice == "No":
        if Score_Of_the_Computer==Score_Of_the_HumanPlayer:
            print("")#A space is given to get a clear output
            print("Marks are Tied")
            print("Score of the computer: ",Score_Of_the_Computer)
            print("Your Score: ",Score_Of_the_HumanPlayer)
            print("No. of Wins by You: " +str (HumanPlayer_wins))#Converting to a string
            print("No. of Wins by the computer: " +str (computer_wins))#Converting to a string
            print("Total number of draws: " +str( Total_draws)) # converting to a string
            print("Total number of games played:" +str(Total_game_plays))#Converting to a string
            print("")#A space is given to get a clear output
            import InsertionOfTheHistory
            InsertionOfTheHistory.InsertionOfTheGameDetails (str(PlayerName),str(HumanPlayer_wins),str(computer_wins),str(Total_draws),str(Total_game_plays))
            
        elif Score_Of_the_Computer>Score_Of_the_HumanPlayer:#Determining the winner
            print("")#A space is given to get a clear output
            print("Bad luck! Computer won!")
            print("Score of the computer: ",Score_Of_the_Computer)
            print("Your Score: ",Score_Of_the_HumanPlayer)
            print("No. of wins by you: " +str (HumanPlayer_wins))#Converting to a string
            print("No. of Wins by the computers: " +str (computer_wins))#Converting to a string
            print("Total number of draws: " +str( Total_draws)) # converting to a string
            print("Total number of games played:" +str(Total_game_plays))#Converting to a string
            print("")#A space is given to get a clear output
            import InsertionOfTheHistory
            InsertionOfTheHistory.InsertionOfTheGameDetails (str(PlayerName),str(HumanPlayer_wins),str(computer_wins),str(Total_draws),str(Total_game_plays))
        else:
            print("")#A space is given to get a clear output
            print("YOU WON!! ")
            print("Score of the computer: ",Score_Of_the_Computer)
            print("Your Score: " ,Score_Of_the_HumanPlayer)
            print("Wins by You: " +str (HumanPlayer_wins))#Converting to a string
            print("Wins by the computer: " +str (computer_wins))#Converting to a string
            print("Total number of draws: " +str( Total_draws)) # converting to a string
            print("Total number of games played:" +str(Total_game_plays))#Converting to a string
            print("")#A space is given to get a clear output
            import InsertionOfTheHistory
            InsertionOfTheHistory.InsertionOfTheGameDetails (str(PlayerName),str(HumanPlayer_wins),str(computer_wins),str(Total_draws),str(Total_game_plays))
        break
            
            
                
