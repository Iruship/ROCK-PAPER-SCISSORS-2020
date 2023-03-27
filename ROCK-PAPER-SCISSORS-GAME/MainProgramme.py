#Calling from a package
import Package.ProcessingTheGame

#Creating and initialyzing the variables
choiceList =("Rock","Paper","Scissors")
PlayerName=""

#Getting the player's name (input)
PlayerName=input("Hello! Enter your Name:")

#Calling the entire "rules" module
import rules

#Calling "RulesOfTheGame" inside "rules" 
rules.RulesOfTheGame()

#Calling "ProcessingTheGame" inside ProcessingTheGame
Package.ProcessingTheGame.ProcessingTheGame(choiceList,PlayerName)
