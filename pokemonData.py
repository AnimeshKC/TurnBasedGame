#Data for the pokemon game

import time
import random as r
#import pygame as py
#Pokemon Class
class Pokemon():
    """Performs the tasks involving the player's information and the first 
    pokemonin the player list"""
    def __init__(self,playerName,playerList):
        self.playerName = playerName
        self.playerList = playerList
        
        #Get the various values for the first pokemon in the list
        self.pokemonName = playerList[0][0]
        self.health = playerList[0][1]
        self.attack = playerList[0][2]
        self.defence = playerList[0][3]
        self.speed = playerList[0][4]
        self.move1 = playerList[0][5]
        self.move2 = playerList[0][6]
        self.move3 = playerList[0][7]
        self.move4 = playerList[0][8]
    def __str__(self):
        string = ("\nName:" + str(self.playerName)
        + "\nYour current Pokemon is:"
        + str(self.pokemonName) + "\nWith the following hp:"
        + str(self.health)+ "\nYour moves are:"
        + "\n1:" + str(self.move1) + "\n2:"
        + str(self.move2) + "\n3:" + str(self.move3)
        + "\n4:" + str(self.move4))
        time.sleep(1)
        return string
    def getTeam(self):
        """Prints the initial list of each player with the three pokemon."""
        
        print ("\n"+ str(self.playerName)+ ", Your pokemon are: ")
        time.sleep(2)
        
        for i in range (len(self.playerList)-1):
            print (str(self.playerList[i][0])+", ")  
        print ("and "+ str(self.playerList[-1][0]))
    def getPokemonName(self):
        return self.pokemonName
    def getHp(self):
        return self.health
    def selectMove(self,userInput):
        while True:
            try:
                output = int(input(userInput))
                if output == 1:
                    selectedMove = self.move1
                elif output == 2:
                    selectedMove = self.move2
                elif output == 3:
                    selectedMove = self.move3
                elif output == 4:
                    selectedMove = self.move4
                return selectedMove
            except:
                pass       
    def takeDamage(self, damageAmount=int, defendValue=int):
        time.sleep(1)
        dmg = damageAmount
        if damageAmount >= defendValue:
            dmg -= defendValue
        elif damageAmount < defendValue:
            dmg = 0
        print(str(self.pokemonName)+ " takes "+
              str(dmg)+ " damage.")    
        self.health -= dmg
    def heal(self, healValue):
        print("\n"+ str(self.pokemonName) +" healed for "
              +str(healValue) + "HP.")
        self.health += healValue
    def atk(self,attackValue, accuracy=100):
        
        time.sleep(1)
        hitchance = r.randrange(0,100)
        
        #Determine whether the move hits or misses 
        
        if hitchance <= accuracy:
            print ("\n"+str(self.pokemonName)+ "'s move hit!")
            damageAmount = attackValue
            damageAmount += self.attack
        
        elif hitchance > accuracy:
            print (str(self.pokemonName)+ "'s move missed!")
            #No damage if the move misses
            damageAmount = 0
        
        return damageAmount        
    def fainted(self):        
        #Determine whether the pokemon fainted
        
        if self.health > 0:
            state = False
    
        if self.health <= 0:
            state = True
        
        return state
#End of pokemon class

#Sprite Class
class Sprite():
    def __init__(self,sprite):
        self.image = sprite
    def draw(self,position,scr):
        self.image.set_colorkey(BLACK)
        scr.blit(self.image, [position[0],position[1]])
        
        
        
#Moveset = "Move":[[minValue,maxValue],"string",accuracy,True (if a healing move)        
moveset = {"Earthquake":[[95,105],"95-105",100],
           "MegaPunch": [[110,120],"110-120",85],
           "Thunder": [[115,135],"115-135",75],
           "MegaKick": [[115,125],"115-125",80],
           "Recover": [[90,120],"(Heal) 90-125",100,True],
           "Return": [[100,100],"100",100],
           "Magnitude": [[40,180],"40-180",100],
           "SoftBoiled": [[70,140],"(Heal) 75-140",100,True],
           "BlastBurn": [[145,155],"145,155",50],
           "HydroPump": [[120,120],"120",80],
           "Blizzard": [[105,125],"105-125",85],
           "JumpKick": [[100,110],"100-110",95],
           "Psychic":  [[95,115],"95-115",95],
           "GunkShot": [[120,130],"120-130",75],
           "BlazeKick": [[110,110],"110",90],
           "StoneEdge": [[110,130],"110-130",80],
           "HydroCannon": [[150,150],"150",100],
           "HiddenPower": [[90,110], "90-110", 100],
           "FocusBlast":[[120,140],"120-140",70],
           "ShadowBall": [[105,105],"105",95],
           "FrenzyPlant": [[140,160],"140-160",50]}
#End of moveset

#Set up the sprites


#List of pokemon
pokemonList = [ #[PokemonName, HP, Attackvalue, DefenseValue, Speed,Move1,Move2,Move3,Move4]
                ["Feraligatr", 270, 33, 27, 26,"HydroPump","HydroCannon","FocusBlast","Return"],
                ["Blaziken", 260, 35, 21, 27,"BlastBurn", "Earthquake", "BlazeKick", "JumpKick"],
                ["Venusaur", 260, 30, 29, 27,"FrenzyPlant","Recover","GunkShot","HiddenPower"],
                ["Snorlax", 420, 34, 27, 19, "Return", "MegaPunch","MegaKick","Recover"],
                ["Mew",  300, 32, 28, 32,"Psychic", "FocusBlast", "SoftBoiled", "HiddenPower"],
                ["Jolteon", 230, 33, 25, 38,"Thunder","HiddenPower","Return","FocusBlast"],
                ["Shuckle", 200, 20 , 50, 18,"StoneEdge","Earthquake","Recover","HiddenPower"],
                ["Blissey", 610,20 , 25, 20,"SoftBoiled","ShadowBall","Psychic","HiddenPower"],
                ["Pikachu", 200, 50, 16, 30,"Thunder", "MegaPunch", "MegaKick", "Return"],
                ["Hitmonlee", 200, 36, 26, 28,"JumpKick","StoneEdge","Earthquake","BlazeKick"],
                ["Aggron", 240, 34, 34, 20,"Earthquake","StoneEdge","MegaPunch","MegaKick"],
                ["Dragonite", 282, 37, 27, 27,"Blizzard","Earthquake","Thunder","StoneEdge"],
                ["Golemn", 260, 36, 28, 20,"Earthquake","StoneEdge","Magnitude","MegaKick"],
                ["Gengar", 220, 38, 19, 34,"ShadowBall","GunkShot","FocusBlast","Psychic"],
                ["Starmie", 259, 32, 25, 35,"Blizzard","Recover","HydroPump","Psychic"]]
#End of Pokemon List
