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
confirmBlackjack = ["1", "2", "3"]
playerHand = []
dealerHand = []
def addCard(x):
    card1 = random.randint(0, len(deck)-1)
    card = cards(deck[card1].split()[0], deck[card1].split()[1])
    deck.remove(str(card.number + " " + card.symbol))
    x.append(card.number + " " + card.symbol)
    
def checkWinner(playerHand):
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
    elif sum(dealerHand) < sum(playerHand):
        print("You win!")
def bustedSplit(a, b, c):
    return True if a == True and b == True and c == True else False

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
        addCard(deckDealer)
    print(deckPlayer[0].split()[0])
    print(deckPlayer[1].split()[1])
    splitable = True if deckPlayer[0].split()[0] == deckPlayer[1].split()[0] else False
    if splitable == True:
        confirmBlackjack.append("4")
    print("Dealer's hand: ???", deckDealer[1])
    print("Your hand: ", deckPlayer[0], deckPlayer[1])
    playerBusted = False
    playerBusted2 = False
    playerBusted3 = False
    dealerBusted = False
    splitted = False
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
        play = input("1. Stand\n2. Hit\n3. Double\nSelect one option [1-3]: " if splitable == False else "1. Stand\n2. Hit\n3. Double\n4. Split\nSelect one option [1-4]: ")
        while play not in confirmBlackjack:
            play = input("1. Stand\n2. Hit\n3. Double\nSelect one option [1-3]: " if splitable == False else "1. Stand\n2. Hit\n3. Double\n4. Split\nSelect one option [1-4]: ")
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
            break
        elif play == "4":
            splitted = True
            deckPlayer2 = []
            deckPlayer2.append(deckPlayer[0])
            deckPlayer3 = []
            deckPlayer3.append(deckPlayer[1])
            playerHand2 = []
            playerHand3 = []
            addCard(deckPlayer2)
            addCard(deckPlayer3)
            print("\nFirst hand: " + " ".join(deckPlayer2))
            print("Second hand: " + " ".join(deckPlayer3))
            while True:
                playerHand2.clear()
                for i in deckPlayer2:
                    card = cards(i.split()[0], i.split()[1])
                    playerHand2.append(card.val())
                if 0 in playerHand2:
                    playerHand2.append(11 if sum(playerHand2)<11 else 1)
                print("Your cards (1st hand): " + " ".join(deckPlayer2))
                print(sum(playerHand2))
                if sum(playerHand2)>21:
                    playerBusted2 = True
                    print("1st hand Busted!")
                    break 
                play2 = input("For 1st hand\n1. Stand\n2. Hit\n3. Double\nSelect one option [1-3]: ")
                if play2 == "1":
                    break
                elif play2 == "2":   
                    addCard(deckPlayer2)
                    continue
                elif play2 == "3":
                    addCard(deckPlayer2)
                    carddouble = cards(deckPlayer2[-1].split()[0], deckPlayer2[-1].split()[1])
                    playerHand2.append(carddouble.val())
                    if 0 in playerHand2:
                        playerHand2.append(11 if sum(playerHand2)<11 else 1)
                    print("Your cards: First hand: " + " ".join(deckPlayer2) + " Second hand: " + " ".join(deckPlayer3))
                    print(sum(playerHand2)) 
                    if sum(playerHand2)>21:
                        playerBusted2 = True
                        print("1st hand Busted!")
                        break
                
            while True:
                playerHand3.clear()
                for i in deckPlayer3:
                    card = cards(i.split()[0], i.split()[1])
                    playerHand3.append(card.val())
                if 0 in playerHand3:
                    playerHand3.append(11 if sum(playerHand3)<11 else 1)
                print("Your cards: Second hand: " + " ".join(deckPlayer3))
                print(sum(playerHand3))
                if sum(playerHand3)>21:
                    playerBusted3 = True
                    print("2nd hand Busted!")
                    break 
                play3 = input("For 2nd hand:\n1. Stand\n2. Hit\n3. Double\nSelect one option [1-3]: ")
                if play3 == "1":
                    break
                elif play3 == "2":   
                    addCard(deckPlayer3)
                    continue
                elif play3 == "3":
                    addCard(deckPlayer3)
                    carddouble = cards(deckPlayer3[-1].split()[0], deckPlayer3[-1].split()[1])
                    playerHand3.append(carddouble.val())
                    if 0 in playerHand3:
                        playerHand3.append(11 if sum(playerHand3)<11 else 1)
                    print("Your cards: " + " ".join(deckPlayer3))
                    print(sum(playerHand3)) 
                    if sum(playerHand3)>21:
                        playerBusted3 = True
                        print("2nd hand Busted!")
                        break
            break
        
        
    if playerBusted == False and bustedSplit(playerBusted2, playerBusted3, splitted)==False:
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


    if splitted == True:
        if dealerBusted == True:
            if len(deckPlayer2) == 2 and sum(playerHand2) == 21:
                print("Congrats! You have BlackJack on hand 1! You win!")
            elif len(deckPlayer3) == 2 and sum(playerHand3) == 21:
                print("Congrats! You have BlackJack on hand 2! You win!")
            elif playerBusted2 == True and playerBusted3 == False:
                print("You busted your first hand, but your second hand won!")
            elif playerBusted3 == True and playerBusted2 == False:
                print("You busted your second hand, but your first hand won!")

        elif dealerBusted == False:
            if playerBusted2 == True and playerBusted3 == True:
                print("You busted all of your hands! You lost!")
            elif playerBusted2 == False and playerBusted3 == False:
                print("Hand 1: ")
                checkWinner(playerHand2)
                print("Hand 2:")
                checkWinner(playerHand3)
            elif playerBusted2 == False and playerBusted3 == True:
                print("Hand 1: ")
                checkWinner(playerHand2)
                print("Hand 2: Busted")
            elif playerBusted2 == True and playerBusted3 == False:
                print("Hand 1: Busted")
                print("Hand 2: ")
                checkWinner(playerHand2)
            
    elif splitted == False:
        if dealerBusted == True:
            if len(deckPlayer) == 2 and sum(playerHand) == 21:
                print("Congrats! You have BlackJack! You win!")
            else:
                print("You win!")
        if playerBusted == True:
            if len(deckDealer) == 2 and sum(dealerHand) == 21:
                print("Dealer has BlackJack! You lose!")
            else:
                print("You lost!")
        if playerBusted == False and dealerBusted == False:
            checkWinner(playerHand)
    playagain = input("Wanna play again?")
    if playagain == "n":
        break
    else:
        continue
    
    
