#Pokemon Style Game
#Animesh KC

import time
import random as r
import pokemonData as pd


#Get the pokemon list and moveset list from the pokemonData file.
pokemonList = pd.pokemonList
moveset = pd.moveset

#The lists for the players.
p1List = []
p2List = []

#Main function
def main():
    
    #Set up the players
    player1 = input("Enter the name of the first player:")
    player2 = input("Enter the name of the second player:")
    
    #Call the initialize function, set up the classes, and display the teams
    initialize(player1,player2)
    p1Class = pd.Pokemon(player1,p1List)
    p2Class = pd.Pokemon(player2,p2List)    
    
    #Display the teams
    p1Class.getTeam()
    p2Class.getTeam()
    
    #Print the two classes which display the information for the first pokemon.
    print ("The game can now begin!")
    time.sleep(2)
    print (p1Class)
    print (p2Class)
    
    #Allow the players to choose their first move.
    p1SelectedMove = p1Class.selectMove((str(player1)+ ", choose a number for a corresponding move:"))
    p2SelectedMove = p2Class.selectMove((str(player2)+ ", choose a number for a corresponding move:"))
    
    print ("The battle may now begin...")
    time.sleep(2)
    
    #Set up the loop for the game
    loop = True
    while loop:
        theGame = battleRound(p1Class,p2Class,p1SelectedMove,p2SelectedMove)
        
        if not theGame[2]:
            print ("Good Game.")
            loop = False
        
        if theGame[2]:
            
            #Create new classes based on what BattleRound returns
            p1Class = theGame[0]
            p2Class = theGame[1]
            
            print ("\nAnother round will commence...")
            time.sleep(2)

            #Once again, print the values for each player's current pokemon.
            print (p1Class)
            print (p2Class)
            
            #Set the selected moves for another round of the loop
            p1SelectedMove = p1Class.selectMove((str(p1Class.playerName)+ ", choose a number for a corresponding move:"))
            p2SelectedMove = p2Class.selectMove((str(p2Class.playerName)+ ", choose a number for a corresponding move:"))
#End of main function

#Initialize function
def initialize(player1,player2):
    """Obtains the initial values of the two players.
    Returns no value. """
    #Introduce the game. 
    time.sleep(1)
    
    print ("\nWelcome to this Pokemon Simulator Game")
    time.sleep(1.5)
    
    print ("Each player will take turns choosing a pokemon until both have three pokemon.")
    time.sleep(1.5)
    
    print("Each pokemon will have its own stats and four moves")
    time.sleep(1.5)
    
    #Introduce the available moves
    print("\nFor reference, here are all the available moves:")
    
    time.sleep(2)
    for key in moveset.keys():
        print ("\n"+key + ":" +"\nMove value:" + str(moveset[key][1])
               + "\nAccuracy:" + str(moveset[key][2]))
    time.sleep(2)
    #Let the players choose the pokemon
    
    selectPokemon(player1,pokemonList,p1List,"first")
    
    selectPokemon(player2,pokemonList,p2List,"first")

    selectPokemon(player1,pokemonList,p1List,"second")

    selectPokemon(player2,pokemonList,p2List,"second")
    
    selectPokemon(player1,pokemonList,p1List,"third")
    
    selectPokemon(player2,pokemonList,p2List,"third")
#End of initialize function

#BattleRound function
def battleRound(class1,class2,move1,move2):
    """Performs a single round.
    key arguments:
    class1 -- class of player1
    class2 -- class of player2
    move1 -- move of player1
    move2 -- move of player2
    
    If the game is over, returns [None,None,False]
    If the game is not over, returns [modified class1, modified class2,True]
    """
    
    #Set GameOn as a variable which determines whether the game is over.
    gameOn = True
    
    #Get the lists of each move from the moveset dictionary
    moveList1 = moveset[move1]
    moveList2 = moveset[move2]
    
    #Perform speed algorithims to determine which player goes first
    
    #First Class is the class whose pokemon moves first
    #Second Class is the class whose pokemon moves second
    
    if class1.speed > class2.speed:
        firstClass = class1
        firstMove = moveList1
        secondClass = class2
        secondMove = moveList2
        print("\n"+ class1.pokemonName + " outspeeds "
              + class2.pokemonName)

    elif class2.speed > class1.speed:
        firstClass = class2
        firstMove = moveList2
        secondClass = class1
        secondMove = moveList1
        print ("\n" + class2.pokemonName + " outspeeds "
               + class1.pokemonName)
    
    elif class1.speed == class2.speed:
            
            #Randomly choose who goes first
            speedTie = r.randrange(1,3)
            
            if speedTie == 1:
                firstClass = class1
                firstMove = moveList1
                secondClass = class2
                secondMove = moveList2
                print ("\n"+ class1.pokemonName +
                       " wins the speed tie")
            elif speedTie ==2:
                firstClass = class2
                firstMove = moveList2
                secondClass = class1
                secondMove = moveList1
                print ("\n"+ class2.pokemonName +
                       "wins the speed tie")
                
    #Set up the lists and the attacks
    firstList = firstClass.playerList
    secondList = secondClass.playerList
    firstMoveAttack = r.randrange(firstMove[0][0],firstMove[0][1]+1)
    secondMoveAttack = r.randrange(secondMove[0][0],secondMove[0][1]+1)    
    
    #First Class Player moves        
    print ("So, " +  str(firstClass.playerName) + " will attack first")
    time.sleep(1)
    
    #If the length of the first move List is 3, the move is an attack move
    if len(firstMove) ==3:
        #Generate damage and make the other pokemon take damage
        attackDamage = firstClass.atk(firstMoveAttack,firstMove[2])
        secondClass.takeDamage(attackDamage,secondClass.defence)
        
        #Check whether the second pokemon has fainted
        check2 = checkFainted(secondClass,secondList)
        
        if not check2:
            
            #Allow the second pokemon to attack since it has not fainted
            print("\nNow,"+ str(secondClass.playerName)+ " will attack")
            
            if len(secondMove) ==3:
                attackDamage = secondClass.atk((secondMoveAttack),(secondMove[2]))
                firstClass.takeDamage(attackDamage,firstClass.defence)
                check1 = checkFainted(firstClass,firstList)
                if check1:
                    checkGameOver1 = checkGameOver(firstClass,firstList)
                    
                    if checkGameOver1:
                        #If the player has no more pokemon, end the game.
                        gameOn = False
                    
                    elif not checkGameOver1:
                        #If the player still has another pokemon, remove the fainted pokemon
                        firstList.remove(firstList[0])
                        firstClass = pd.Pokemon(firstClass.playerName,firstList)
                        gameOn = True
            
            elif len(secondMove) == 4:
                secondClass.heal(secondMoveAttack)
        elif check2:
            checkGameOver2 = checkGameOver(secondClass,secondList)
            if checkGameOver2:
                gameOn = False
            elif not checkGameOver2:
                secondList.remove(secondList[0])
                secondClass = pd.Pokemon(secondClass.playerName,secondList)
                gameOn = True
    
    #if the length of the moveList is 4, the player uses a healing move.
    elif len(firstMove) ==4:
        firstClass.heal(firstMoveAttack)
           
        #Second Player  now uses a move
        if len(secondMove) ==3:
            attackDamage = secondClass.atk(secondMoveAttack,secondMove[2])
            firstClass.takeDamage(attackDamage,firstClass.defence)
            check1 = checkFainted(firstClass,firstList)
            
            if check1:
                checkGameOver1 = checkGameOver(firstClass,firstList)
                
                if checkGameOver1:
                    gameOn = False
                
                elif not checkGameOver1: 
                    firstList.remove(firstList[0])
                    firstClass = pd.Pokemon(firstClass.playerName,firstList)    
                    gameOn = True
        
        elif len(secondMove) ==4:
            healAmount = secondClass.heal(secondMoveAttack)
    
    if not gameOn:
        return [None,None,False]
    
    elif gameOn == True:
        return [firstClass,secondClass,True]
#End of BattleRound function


def pokemonIntInput(prompt):
    while True:
        try:
            output = int(input(prompt))
            if output <= len(pokemonList):
                return output
        except:
            pass


def pokemonChoice(aList):
    """Displays the information for each pokemon in the list"""
    for i in range (len(aList)):    
        print ("\n" + str(i+1)+ ":" + str(aList[i][0]) +"\nHp:" + str(aList[i][1])
                + "\nAttack:" + str(aList[i][2]) + "\nDefense:" + str(aList[i][3])
                + "\nSpeed:" + str(aList[i][4]) + "\nMove1:" + str(aList[i][5])
                + "\nMove2:" + str(aList[i][6]) + "\nMove3:" + str(aList[i][7])
               +"\nMove4:" + str(aList[i][8]) + "\n")


def selectPokemon(player,originalList,playerList,orderString):
    print( "\n" + str(player)+ ", here is your " + str(orderString) + " choice of pokemon...")
    time.sleep(2)
    pokemonChoice(pokemonList)
    chosenNum = pokemonIntInput (str(player)+ ", Choose a number for your " + str(orderString)+ " pokemon:")
    indexNum = chosenNum-1
    playerList.append(originalList[indexNum])
    originalList.remove(originalList[indexNum])
    time.sleep(1)

def listChange(chosenNum,initialList, playerList):
    #Generate index number by subvtracting one from the chosen number
    indexnum = chosenNum-1
    #Append to player's list and remove that pokemon from the pokemon list
    playerList.append(initialList[indexnum])
    initialList.remove(initialList[indexnum])
    
def checkFainted(playerClass,playerList):  
    time.sleep(0.5)
    if playerClass.fainted():
        print (str(playerClass.pokemonName) + " has fainted.")
        return True
    elif not playerClass.fainted():
        return False

def checkGameOver(thePlayerClass,thePlayerList):
    time.sleep(0.5)
    if len(thePlayerList) > 1:
        print ("\nThe game continues")
        return False
    elif len(thePlayerList) ==1:
        print ("The game is over")
        print ("No more pokemon remain for " + str(thePlayerClass.playerName))
        return True



main()
 





