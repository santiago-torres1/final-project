# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:32:02 2022

@author: Santiago
"""

from time import sleep

yesno = ["YES", "Y", "NO", "N"]
player = {"totalPayment" : 0}
chips = { "1" : ["100" , 1.00], "2" : ["200" , 2.00], "3" : ["500" , 5.00],
         "4" : ["1000" , 10.00], "5" : ["5000" , 50.00], "6" : ["Custom Amount" , 0.00]}
paymentMethod = {"1" : "Cash", "2" : "Debit/Credit card", "3" : "Crypto (BTC/ETH)"}
games = {"1" : "Roulette", "2" : "BlackJack", "3" : "Texas Hold'em Poker"}

def addChips():
    while True:
        print("How many chips would you like? (100 chips = $1): ")
        for k in chips.keys():
            print("{}. {}".format(k, chips[k][0]))
        money = input("Select one (1-6): ")
        while money not in chips.keys():
            money = input("Select one (1-6): ")
        if money == "6":
            while True:
                try:
                    custom = int(input("Please enter your amount. Only multiples of 100 allowed. (Min: 100. Max: 50000.): "))
                except:
                    print("Please enter a valid value!")
                else:
                    if custom%100 != 0:
                        continue
                    else:
                        break        
        payment = int(custom) / 100 if money == "6" else chips[money][1]
        player["totalPayment"] = payment if player["totalPayment"] == 0 else player["totalPayment"]+payment
        print ("Total payment: ${:.2f}".format(player["totalPayment"]))
        more = input("Would you like to add more chips? [y/n]: ")
        while more.strip().upper() not in yesno:
            more = input("Would you like to add more chips? [y/n]: ")
        if more.strip().upper() == "Y":
            continue
        else:
            break

def makePayment():
    print ("Now, how would you like to pay?: ")
    for k, v in paymentMethod.items():
        print("{}. {}".format(k, v))
    method = input("Select one [1-3]: ")
    while method not in paymentMethod.keys():
        method = input("Select one [1-3]: ")
    for i in range(0, 3):
        print(".")
        sleep(0.8 if method=="2" else 0.2)
    print("Payment received!")

def chooseGame():
    for k, v in games.items():
        print("{}. {}".format(k, v))
    game = input("Please select one [1-3]: ")
    while game not in games.keys():
        game = input("Please select one [1-3]: ")
    print("Okay {}! Let's play {}...".format(name, games[game]))
    instructions = input("Enter [i] to display the {}")
    
class cards:
    def __init__(self, color, figure, number):
        self.color = color
        self.figure = figure
        self.number = number
        
#class dealer:
    
#class bet:
    
#class player:
    

print("Welcome to Waterloo Casino!")
name = input("What's your name?: ")
addChips()
makePayment()
print ("Thanks {}! Now, what would you like to play today?".format(name))
chooseGame()
