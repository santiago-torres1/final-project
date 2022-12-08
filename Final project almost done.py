# -*- coding: utf-8 -*-
"""
Title: Final project.py
Author: Santiago Torres
Date created: 11/30/2022
Date last modified: 12/07/2022
This program is a virtual casino. It will ask the user for the name, the amount of chips they want, and the payment method.
Then, the user can choose to play two games: Roulette and blackjack. Whenever the user runs out of chips, the program will
ask if they want to add more. If not, the program ends.
"""

from time import sleep #Importing modules to use later. Sleep for delays, random for random values
import random
from time import localtime

#Declaring dictionaries and lists that will be used later.
yesno = ["YES", "Y", "NO", "N"] #List for input checking.
playerData = {"totalPayment" : 0, "totalChips" : 0} #Dictionary for storing player's data
chips = { "1" : [100 , 1.00], "2" : [200 , 2.00], "3" : [500 , 5.00],
         "4" : [1000 , 10.00], "5" : [5000 , 50.00], "6" : ["Custom Amount" , 0.00]} #Dictionary for showing options to buy chips
paymentMethod = {"1" : "Cash", "2" : "Debit/Credit card", "3" : "Crypto (BTC/ETH)"} #Dictionary for showing payment methods
games = {"1" : "Roulette", "2" : "BlackJack"} #Dictionary for showing games#The 4 following lists will be used for creating class card objects.
deck = [] #This lists will be used in BlackJack function
deckPlayer = []
deckDealer = []
letters = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] #This lists will be used for creating class cards objects
symbols2 = ["", "♣", "♦", "♠", "♥"]
confirmBlackjack = ["1", "2", "3"] 
playerHand = []
dealerHand = []

def addCard(x): # This function will add a card to the deck in BlackJack game
    card1 = random.randint(0, len(deck)-1)
    card = cards(deck[card1].split()[0], deck[card1].split()[1])
    deck.remove(str(card.number + " " + card.symbol))
    x.append(card.number + " " + card.symbol)

def addChips(): #This function is for adding chips to the user's balance
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
        playerData["totalPayment"] = payment if playerData["totalPayment"] == 0 else playerData["totalPayment"]+payment
        playerData["Chips"] = custom if money == "6" else chips[money][0]
        playerData["totalChips"] = playerData["Chips"] if playerData["totalChips"] == 0 else playerData["totalChips"] + playerData["Chips"]
        global player1
        player1 = player(name, (custom if money == "6" else chips[money][0]), playerData["totalPayment"])
        print ("Total payment: ${:.2f}".format(playerData["totalPayment"]))
        more = input("Would you like to add more chips? [y/n]: ")
        while more.strip().upper() not in yesno:
            more = input("Would you like to add more chips? [y/n]: ")
        if more.strip().upper() == "Y":
            continue
        else:
            break

def bustedSplit(a, b, c): #This function is for condition checking in BlackJack game
    return True if a == True and b == True and c == True else False

def makePayment(): #This function is for "making" a payment
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
    receipt = open("receipt.txt", "w")
    timetoday = localtime()
    receipt.write("\n{0: ^60s}".format("Purchase date: {}/{}/{}".format(timetoday.tm_mon, timetoday.tm_mday, timetoday.tm_year)))
    receipt.write("\n{0: ^60s}".format("Purchase time: {}:{}".format(timetoday.tm_hour, timetoday.tm_min)))
    receipt.write("\n{0: ^60s}".format("Player's name: {}".format(name)))
    receipt.write("\n{0: ^60s}".format("Payment method: {}".format(paymentMethod[method])))
    receipt.write("\n{0:-^60s}".format(''))
    receipt.write("\n{} \t \t {} \t {}".format("ITEM", "AMOUNT", "PRICE").expandtabs(17))
    receipt.write("\n{} \t \t {} \t ${:.2f}".format("Chips", playerData["totalChips"], playerData["totalChips"]/100).expandtabs(17))
    receipt.write("\n{0:-^60s}".format(''))
    receipt.write("\n \t {}".format("SUBTOTAL: ").expandtabs(25) + "\t ${:.2f}".format(playerData["totalChips"]/100).expandtabs(15))
    receipt.write("\n \t {}".format("TAX (HST 13%): ").expandtabs(25) + "\t ${:.2f}".format(0.13*playerData["totalChips"]/100).expandtabs(11))
    receipt.write("\n \t {}".format("TOTAL: ").expandtabs(25) + "\t ${:.2f}".format(1.13*playerData["totalChips"]/100).expandtabs(18))
    receipt.close()
    receiptview = input("Would you like to see your receipt? [y/n]: ")
    while receiptview.strip().upper() not in yesno:
        receiptview = input("Would you like to see your receipt? [y/n]: ")
    if receiptview.strip().upper() == "YES" or receiptview.strip().upper() == "Y":
        receipt2 = open("receipt.txt", "r")
        sleep(1)
        print(receipt2.read())
        sleep(1)

def checkWinner(playerHand, bet): #This function is for checking the winner in BlackJack game
    if len(deckPlayer) == 2 and sum(playerHand) == 21 and len(deckDealer) == 2 and sum(dealerHand) == 21:
        print("Push!")
        player1.chips = player1.chips + bet
        print("Your new balance is: {}".format(player1.chips))
    elif len(deckDealer) == 2 and sum(dealerHand) == 21:
        print("Dealer has BlackJack! You lose!")
        print("You lost {} chips. New balance: {}".format(bet, player1.chips))
    elif len(deckPlayer) == 2 and sum(playerHand) == 21:
        print("Congrats! You have BlackJack! You win!")
        winnings = 1.5*bet if (1.5*bet)%100 == 0 else 2*bet
        player1.chips = player1.chips + winnings
        print("You have won {} chips. New balance: {}".format(winnings, player1.chips))
    elif sum(dealerHand) > sum(playerHand):
        print("You lost!")
        print("You lost {} chips. New balance: {}".format(bet, player1.chips))
    elif sum(dealerHand) == sum(playerHand):
        print("Push!")
        player1.chips = player1.chips + bet
        print("Your new balance is: {}".format(player1.chips))
    elif sum(dealerHand) < sum(playerHand):
        print("You win!")
        player1.chips = player1.chips + 2*bet
        print("You won {} chips. Your new balance is: {}".format(2*bet, player1.chips))

def chooseGame(): #This function is for choosing a game, and displaying its instructions if requested by user.
    for k, v in games.items():
        print("{}. {}".format(k, v))
    global game
    game = input("Please select one [1-2]: ")
    while game not in games.keys():
        game = input("Please select one [1-2]: ")
    print("Okay {}! Let's play {}...".format(name, games[game]))
    instructions = input("Type [i] to display the {} instructions. Press enter or type any key to continue to the game: ".format(games[game]))
    if instructions.strip().upper() == "I":
        file = (games[game] + ".txt")
        inst = open(file, "r")
        listInst = inst.readlines()
        for i in range (0, len(listInst)):
            print(listInst[i])
            sleep(2)
        input("Press enter to start game.")
        
def betSlotColor(color): #This function is used for getting
    return "Black" if color == "1" else "Red" if color == "2" else "Green"

def betSlot(number): #This function is for getting 
    return "3" if number == 0 else "1" if number%2 == 0 else "2"
    
def rouletteGame(): #This function is the whole roulette game.
    while True:
        betColor = input("Please select your the color that you want [1: Black / 2: Red / 3: Green]: ")
        while betColor != "1" and betColor != "2" and betColor != "3":
            betColor = input("Please select your the color that you want [1: Black / 2: Red / 3: Green]: ")
        print ("Your current number of chips is: {}".format(player1.chips))
        while True:    
            try:
                bet = int(input("Please enter your bet (Bet must be a multiple of 100): "))
            except:
                print("Bet should be a number! ")
            else:
                if bet%100 != 0:
                    print("Bet not valid. Bet must be a multiple of 100")
                    continue
                elif bet>player1.chips:
                    print("Bet not valid. You don't have enough chips!")
                    continue
                else:
                    newBet = slot(betColor)
                    print ("Your bet of {} to {} has been placed. We're going all in!!!".format(bet, newBet.betColor)
                           if player1.chips-bet==0 else "Your bet of {} to {} has been placed".format(bet, newBet.betColor))
                    break   
        input("Press enter to spin the roulette!")
        print("spinning...")
        sleep(4)
        print("roulette is stopping...")
        sleep(2)
        print("STOPPED!")
        result = random.randint(0, 18)
        print("{} - {} !!!!".format(result, betSlotColor(betSlot(result))))
        sleep(1)
        if betSlotColor(betSlot(result)) == newBet.betColor:
            bet = bet*18 if betColor == "3" else bet*2
            player1.chips = player1.chips + bet
            print("You won!!! You have won {} chips. New balance: {}".format(bet, player1.chips))
        else: 
            player1.chips = player1.chips - bet
            print("You lost :(. You have lost {} chips. New balance: {}".format(bet, player1.chips))
        if player1.chips == 0:
            break
        again = input("Do you wanna play the Roulette again? [y/n]: ")
        while again.strip().upper() not in yesno:
            again = input("Do you wanna play the Roulette again? [y/n]: ")
        if again.strip().upper() == "YES" or again.strip().upper() == "Y":
                continue
        else:
                break
        
def blackJackGame(): #This function is the whole blackjack game.
    while True:  
        while True:    
            try:
                print ("Your chips: {}".format(player1.chips))
                bet = int(input("Please enter your bet (Bet must be a multiple of 100): "))
            except:
                print("Bet should be a number! ")
            else:
                if bet%100 != 0:
                    print("Bet not valid. Bet must be a multiple of 100")
                    continue
                elif bet>player1.chips:
                    print("Bet not valid. You don't have enough chips!")
                    continue
                else:
                    print ("Your bet of {} has been placed. We're going all in!!!".format(bet)
                           if player1.chips-bet==0 else "Your bet of {} has been placed".format(bet))
                    player1.chips = player1.chips - bet
                    print ("You have {} chips left.".format(player1.chips))
                    break   
        print("Shuffling...")
        sleep(2)
        deck.clear()
        deckPlayer.clear()
        deckDealer.clear()
        for i in range (0, 13): 
            for j in range (1, 5):
                deck.append(letters[i]+" "+symbols2[j])
                
        for i in range (0, 2):
            addCard(deckPlayer)
            addCard(deckDealer)
        splitable = True if deckPlayer[0].split()[0] == deckPlayer[1].split()[0] else False
        if splitable == True:
            confirmBlackjack.append("4")
        print("\nDealer's hand: ???", deckDealer[1])
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
            print("\nYour hand: " + " ".join(deckPlayer))
            print(sum(playerHand))
            if sum(playerHand)>21:
                playerBusted = True
                print("\nBusted!")
                input("\nPress enter to continue.")
                break
            play = input("\n1. Stand\n2. Hit\n3. Double\n\nSelect one option [1-3]: " if splitable == False else "1. Stand\n2. Hit\n3. Double\n4. Split\nSelect one option [1-4]: ")
            while play not in confirmBlackjack:
                play = input("\n1. Stand\n2. Hit\n3. Double\n\nSelect one option [1-3]: " if splitable == False else "1. Stand\n2. Hit\n3. Double\n4. Split\nSelect one option [1-4]: ")
            if play == "1":
                print("\nYou stood.")
                input("\nPress enter to continue.")
                sleep(1)
                break
            elif play == "2":   
                addCard(deckPlayer)
                print("Hit.")
                sleep(1)
                continue
            elif play == "3":
                if player1.chips - bet < 0:
                    print("\nYou don't have enough chips to double!")
                    continue
                else:
                    player1.chips = player1.chips - bet
                    print("\nYour bet has been doubled! New balance: {}".format(player1.chips))
                    addCard(deckPlayer)
                    carddouble = cards(deckPlayer[-1].split()[0], deckPlayer[-1].split()[1])
                    playerHand.append(carddouble.val())
                    if 0 in playerHand:
                        playerHand.append(11 if sum(playerHand)<11 else 1)
                    sleep(1)
                    print("\nYour cards: " + " ".join(deckPlayer))
                    print(sum(playerHand))
                    if sum(playerHand)>21:
                        playerBusted = True
                        print("\nBusted!")
                        input("\nPress enter to continue.")
                        break

            elif play == "4":
                if player1.chips - bet < 0:
                    print("You don't have enough chips to split!")
                    input("\nPress enter to continue.")
                    continue
                else:
                    player1.chips = player1.chips-bet
                    print("\nYou have splitted your hand. A new bet has been placed. New balance: {}".format(player1.chips))
                    sleep(1)
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
                    print("\nSecond hand: " + " ".join(deckPlayer3))
                    while True:
                        playerHand2.clear()
                        for i in deckPlayer2:
                            card = cards(i.split()[0], i.split()[1])
                            playerHand2.append(card.val())
                        if 0 in playerHand2:
                            playerHand2.append(11 if sum(playerHand2)<11 else 1)
                        print("\nYour hand (1st hand): " + " ".join(deckPlayer2))
                        print(sum(playerHand2))
                        if sum(playerHand2)>21:
                            playerBusted2 = True
                            print("\n1st hand Busted!")
                            input("\nPress enter to continue.")
                            break 
                        play2 = input("\nFor 1st hand\n1. Stand\n2. Hit\n3. Double\n\nSelect one option [1-3]: ")
                        if play2 == "1":
                            break
                        elif play2 == "2":   
                            addCard(deckPlayer2)
                            continue
                        elif play2 == "3":
                            if player1.chips - bet < 0:
                                print("\nYou don't have enough chips to double!")
                                input("\nPress enter to continue.")
                            else:
                                player1.chips = player1.chips - bet
                                print("\nYou have doubled your bet for hand 1. New balance: {}".format(player1.chips))
                                sleep(1)
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
                                    input("\nPress enter to continue.")
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
                            input("\nPress enter to continue.")
                            break 
                        play3 = input("For 2nd hand:\n1. Stand\n2. Hit\n3. Double\nSelect one option [1-3]: ")
                        if play3 == "1":
                            break
                        elif play3 == "2":   
                            addCard(deckPlayer3)
                            continue
                        elif play3 == "3":
                            if player1.chips - bet < 0:
                                print("You don't have enough chips to double!")
                                input("\nPress enter to continue.")
                            else:
                                player1.chips = player1.chips - bet
                                print("You have doubled your bet for hand 2. New balance: {}".format(player1.chips))
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
                                    input("\nPress enter to continue.")
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
                    input("\nPress enter to continue.")
                    break
            
                sleep(1.5)
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
                    winnings = 1.5*bet if (1.5*bet)%100 == 0 else 2*bet
                    player1.chips = player1.chips + winnings
                    print("You have won {} chips. New balance: {}".format(winnings, player1.chips))
                elif len(deckPlayer3) == 2 and sum(playerHand3) == 21:
                    print("Congrats! You have BlackJack on hand 2! You win!")
                    winnings = 1.5*bet if (1.5*bet)%100 == 0 else 2*bet
                    player1.chips = player1.chips + winnings
                    print("You have won {} chips. New balance: {}".format(winnings, player1.chips))
                elif playerBusted2 == True and playerBusted3 == False:
                    print("You busted your first hand, but your second hand won!")
                    winnings = 2*bet
                    player1.chips = player1.chips + winnings
                    print("You have won {} chips. New balance: {}".format(winnings, player1.chips))
                elif playerBusted3 == True and playerBusted2 == False:
                    print("You busted your second hand, but your first hand won!")
                    winnings = 2*bet
                    player1.chips = player1.chips + winnings
                    print("You have won {} chips. New balance: {}".format(winnings, player1.chips))
    
            elif dealerBusted == False:
                if playerBusted2 == True and playerBusted3 == True:
                    print("You busted all of your hands! You lost!")
                elif playerBusted2 == False and playerBusted3 == False:
                    print("Hand 1: ")
                    checkWinner(playerHand2, bet)
                    print("Hand 2:")
                    checkWinner(playerHand3, bet)
                elif playerBusted2 == False and playerBusted3 == True:
                    print("Hand 1: ")
                    checkWinner(playerHand2, bet)
                    print("Hand 2: Busted")
                elif playerBusted2 == True and playerBusted3 == False:
                    print("Hand 1: Busted")
                    print("Hand 2: ")
                    checkWinner(playerHand2, bet)
                
        elif splitted == False:
            if dealerBusted == True:
                if len(deckPlayer) == 2 and sum(playerHand) == 21:
                    print("Congrats! You have BlackJack! You win!")
                    winnings = 1.5*bet if (1.5*bet)%100 == 0 else 2*bet
                    player1.chips = player1.chips + winnings
                    print("You have won {} chips. New balance: {}".format(winnings, player1.chips))
                else:
                    print("You win!")
                    player1.chips = player1.chips + 2*bet
                    print("You won {} chips. Your new balance is: {}".format(2*bet, player1.chips))
            if playerBusted == True:
                if len(deckDealer) == 2 and sum(dealerHand) == 21:
                    print("Dealer has BlackJack! You lose!")
                    print("You lost {} chips. New balance: {}".format(bet, player1.chips))
                else:
                    print("You lost!")
                    print("You lost {} chips. New balance: {}".format(bet, player1.chips))
            if playerBusted == False and dealerBusted == False:
                checkWinner(playerHand, bet)
        if player1.chips > 0:                
            playagain = input("Wanna play BlackJack again?[y/n]: ")
            while playagain.strip().upper() not in yesno:
                playagain = input("Wanna play BlackJack again?[y/n]: ")
            if playagain.strip().upper() == "YES" or playagain.strip().upper() == "Y":
                continue
            else:
                break
        else:
            break
            
            
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
        
class player:
    def __init__(self, name, chips, balance):
        self.chips = chips
        self.balance = balance
        
class slot:
    def  __init__(self, color):
        self.color = color 
        self.betColor = "Black" if self.color == "1" else "Red" if self.color == "2" else "Green"
          
print("Welcome to Waterloo Casino!")
name = input("What's your name?: ")
addChips()
makePayment()
print ("Thanks {}! Now, what would you like to play today?".format(name))
while True:
    chooseGame()
    if game == "1":
        rouletteGame()
    elif game == "2":
        blackJackGame()       
    if player1.chips==0:
        more = input("You have lost all of your chips! Do you wanna purchase more? [y/n]: ")
        while more not in yesno:
            more = input("You have lost all of your chips! Do you wanna purchase more? [y/n]: ")
        if more.strip.upper == "YES" or more.strip.upper == "Y":
            addChips()
            makePayment()
            continue
        else:
            print("You have lost ${:.2f}! Good luck next time.".format(playerData["totalPayment"]))
            break
    else:
        again = input("Do you wanna play another game? [y/n]: ")
        while again.strip().upper() not in yesno:
            again = input("Do you wanna play another game? [y/n]: ")
        if again.strip().upper() == "YES" or again.strip().upper() == "Y":
            continue
        else:
            print("You have cashed out ${:.2f} ({} chips).".format(player1.chips/100, player1.chips))
            print("Thanks for playing at Waterloo Casino! We'll see you soon.")
            break


