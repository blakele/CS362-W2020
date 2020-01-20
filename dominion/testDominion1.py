
# -*- coding: utf-8 -*-
"""
Created on sunday 1/19/2020

@author: lebla
"""

import Dominion
import random
from collections import defaultdict
import testUtility as testUtility
#Get player names
player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
nV, nC = testUtility.getCurseVictory(player_names)

#Define box
box = testUtility.getBoxes(nV)
#test scenaro 1:
#box = testUtility.getBoxes(nC)

supply_order = testUtility.getSupplyOrder()


#Pick 10 cards from box to be in the supply.
supply = testUtility.get10BoxCards(box)

#The supply always has these cards
supply = testUtility.getSupplyCards(player_names, nV, nC, supply)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.setPlayers(player_names)

#Play the game
testUtility.playGame(supply, players, supply_order, trash)
            

#Final score
testUtility.finalScore(players)
