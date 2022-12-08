# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:12:24 2022

@author: Santiago


"""
import random
from time import sleep
deck = []
deckPlayer = []
deckDealer = []
letters = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
symbols2 = ["", "♣", "♦", "♠", "♥"]
playerHand = []
dealerHand = []
def addCard(x):
    card1 = random.randint(0, len(deck)-1)
    card = cards(deck[card1].split()[0], deck[card1].split()[1])
    deck.remove(str(card.number + " " + card.symbol))
    x.append(card.number + " " + card.symbol)

    
class cards:
    def __init__(self, number, symbol):
        self.symbol = symbol
        self.number = number
    def val(self):
        if self.number == "A":
            return 0
        elif self.number == "J" or self.number == "Q" or self.number == "K":
            return 10
        else:
            return int(self.number)
while True:   
    deck.clear()
    deckPlayer.clear()
    deckDealer.clear()
    for i in range (0, 13): 
        for j in range (1, 5):
            deck.append(letters[i]+" "+symbols2[j])
            
    for i in range (0, 2):
        addCard(deckPlayer)
    for i in range (0, 2):
        addCard(deckDealer)
        
    print("Dealer's hand: ???", deckDealer[1])
    print("Your hand: ", deckPlayer[0], deckPlayer[1])
    playerBusted = False
    dealerBusted = False
    while True:
        playerHand.clear()
        for i in deckPlayer:
            card = cards(i.split()[0], i.split()[1])
            playerHand.append(card.val())
        if 0 in playerHand:
            playerHand.append(11 if sum(playerHand)<11 else 1)
        print("Your cards: " + " ".join(deckPlayer))
        print(sum(playerHand))
        if sum(playerHand)>21:
            playerBusted = True
            print("Busted!")
            break
    
        play = input("1. Stand/2. Hit/3. Double")
        if play == "1":
            break
        elif play == "2":   
            addCard(deckPlayer)
            continue
        elif play == "3":
            addCard(deckPlayer)
            carddouble = cards(deckPlayer[-1].split()[0], deckPlayer[-1].split()[1])
            playerHand.append(carddouble.val())
            if 0 in playerHand:
                playerHand.append(11 if sum(playerHand)<11 else 1)
            print("Your cards: " + " ".join(deckPlayer))
            print(sum(playerHand))
            if sum(playerHand)>21:
                playerBusted = True
                print("Busted!")
            break
        
    if playerBusted == False:
        while True:
            dealerHand.clear()
            for i in deckDealer:
                card = cards(i.split()[0], i.split()[1])
                dealerHand.append(card.val())
            if 0 in dealerHand:
                dealerHand.append(11 if sum(dealerHand)<11 else 1)
            print("Dealer's cards: " + " ".join(deckDealer))
            print(sum(dealerHand))
            if sum(dealerHand)>21:
                dealerBusted = True
                print("Dealer busted!")
                break
        
            sleep(0.5)
            if sum(dealerHand)<17:
                if sum(playerHand)<sum(dealerHand):
                    break
                else:
                    addCard(deckDealer)
                    continue
            elif sum(dealerHand)==17:   
                if 0 in dealerHand and len(deckDealer) == 2:
                    addCard(deckDealer)
                    continue
                else:
                    break
            elif sum(dealerHand)>17:
                break
        
    if dealerBusted == True:
        if len(deckPlayer) == 2 and sum(playerHand) == 21:
            print("Congrats! You have BlackJack! You win!")
        else:
            print("You win!")
    if playerBusted == True:
        if len(deckDealer) == 2 and sum(dealerHand) == 21:
            print("Dealer has BlackJack! You lose!")
        print("You lost!")
    if playerBusted == False and dealerBusted == False:
        if len(deckPlayer) == 2 and sum(playerHand) == 21 and len(deckDealer) == 2 and sum(dealerHand) == 21:
            print("Push!")
        elif len(deckDealer) == 2 and sum(dealerHand) == 21:
            print("Dealer has BlackJack! You lose!")
        elif len(deckPlayer) == 2 and sum(playerHand) == 21:
            print("Congrats! You have BlackJack! You win!")
        elif sum(dealerHand) > sum(playerHand):
            print("You lost!")
        elif sum(dealerHand) == sum(playerHand):
            print("Push!")
        else:
            print("You win!")
    playagain = input("Wanna play again?")
    if playagain == "n":
        break
    else:
        continue
    
    
