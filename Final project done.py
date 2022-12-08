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
    card1 = random.randint(0, len(deck)-1) #Picking card number and symbol from deck
    card = cards(deck[card1].split()[0], deck[card1].split()[1]) #Creating object of class card.
    deck.remove(str(card.number + " " + card.symbol)) #Removing that card of deck
    x.append(card.number + " " + card.symbol) #Adding the card to the desired list (player or dealer) depending on the situation

def addChips(): #This function is for adding chips to the user's balance
    while True: #This loop is in case the player wants to add more chips
        print("How many chips would you like? (100 chips = $1): ")
        for k in chips.keys():
            print("{}. {}".format(k, chips[k][0])) #Printing the options
        money = input("Select one (1-6): ")
        while money not in chips.keys():
            money = input("Select one (1-6): ")
        if money == "6":
            while True:
                try:
                    custom = int(input("Please enter your amount. Only multiples of 100 allowed. (Min: 100. Max: 50000.): ")) #This condition will run if the player wants to purchase a custom amount of chips
                except:
                    print("Please enter a valid value!")
                else:
                    if custom%100 != 0:
                        continue
                    else:
                        break        
        payment = int(custom) / 100 if money == "6" else chips[money][1] #The following lines will add the chips amount and price to the lists for being used later.
        playerData["totalPayment"] = payment if playerData["totalPayment"] == 0 else playerData["totalPayment"]+payment
        playerData["Chips"] = custom if money == "6" else chips[money][0]
        playerData["totalChips"] = playerData["Chips"] if playerData["totalChips"] == 0 else playerData["totalChips"] + playerData["Chips"]
        global player1 #Declaring a global object of class player for being used in the games.
        player1 = player(name, playerData["totalChips"], playerData["totalPayment"])
        print ("Total payment: ${:.2f}".format(playerData["totalPayment"]))
        more = input("Would you like to add more chips? [y/n]: ") #This is in case the user wants to add more chips
        while more.strip().upper() not in yesno:
            more = input("Would you like to add more chips? [y/n]: ")
        if more.strip().upper() == "Y":
            continue
        else:
            break

def bustedSplit(a, b, c): #This function is for condition checking in BlackJack game
    return True if a == True and b == True and c == True else False

def makePayment(): #This function is for "making" a payment. NOT REAL PAYMENTS ARE PROCESSED :P
    print ("Now, how would you like to pay?: ")
    for k, v in paymentMethod.items():
        print("{}. {}".format(k, v)) #Printing payment options
    method = input("Select one [1-3]: ")
    while method not in paymentMethod.keys():
        method = input("Select one [1-3]: ")
    for i in range(0, 3):
        print(".")
        sleep(0.8 if method=="2" else 0.2) #Simulating payment
    print("Payment received!")
    receipt = open("receipt.txt", "w") #This opens a .txt file to print the receipt
    timetoday = localtime()  #This variable stores the data of the current time.
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
    if len(deckPlayer) == 2 and sum(playerHand) == 21 and len(deckDealer) == 2 and sum(dealerHand) == 21: #If both dealer and player have Blackjack.
        print("Push!")
        player1.chips = player1.chips + bet
        print("Your new balance is: {}".format(player1.chips))
    elif len(deckDealer) == 2 and sum(dealerHand) == 21: #If dealer has blackjack
        print("Dealer has BlackJack! You lose!")
        print("You lost {} chips. New balance: {}".format(bet, player1.chips))
    elif len(deckPlayer) == 2 and sum(playerHand) == 21: #If player has blackjack
        print("Congrats! You have BlackJack! You win!")
        winnings = 1.5*bet if (1.5*bet)%100 == 0 else 2*bet
        player1.chips = player1.chips + winnings
        print("You have won {} chips. New balance: {}".format(winnings, player1.chips)) 
    elif sum(dealerHand) > sum(playerHand): #If dealer wins (dealer cards add up more than player's cards, without surpassing 21)
        print("You lost!")
        print("You lost {} chips. New balance: {}".format(bet, player1.chips))
    elif sum(dealerHand) == sum(playerHand): #If there's a tie
        print("Push!")
        player1.chips = player1.chips + bet
        print("Your new balance is: {}".format(player1.chips))
    elif sum(dealerHand) < sum(playerHand): #If player wins
        print("You win!")
        player1.chips = player1.chips + 2*bet
        print("You won {} chips. Your new balance is: {}".format(2*bet, player1.chips))

def chooseGame(): #This function is for choosing a game, and displaying its instructions if requested by user.
    for k, v in games.items(): #Printing options
        print("{}. {}".format(k, v))
    global game #Declaring global variable to be used in the program later.
    game = input("Please select one [1-2]: ")
    while game not in games.keys():
        game = input("Please select one [1-2]: ")
    print("Okay {}! Let's play {}...".format(name, games[game]))
    instructions = input("Type [i] to display the {} instructions. Press enter or type any key to continue to the game: ".format(games[game])) #Asking if the player wants to see the instructions
    if instructions.strip().upper() == "I": #Retrieving instructions from .txt files I have previously written.
        file = (games[game] + ".txt")
        inst = open(file, "r")
        listInst = inst.readlines()
        for i in range (0, len(listInst)):
            print(listInst[i])
            sleep(2.5)
        input("Press enter to start game.")
        
def betSlotColor(color): #This function is used for getting the color of the slot in Roulette
    return "Black" if color == "1" else "Red" if color == "2" else "Green"

def betSlot(number): #This function is for getting the value that will be used in betSlotColor function
    return "3" if number == 0 else "1" if number%2 == 0 else "2"
    
def rouletteGame(): #This function is the whole roulette game.
#The roulette I created here is slightly different from a casino's roulette (It is a more simple version). It has 19 slots (numbers 0-18) instead of usual 37 or 38. Also,
#a bet can only be placed to a color (no bet for individual numbers or group of numbers). Even numbers are black, odd numbers are red, 0 is green.
    while True:
        betColor = input("Please select your the color that you want [1: Black / 2: Red / 3: Green]: ") #First, the player must choose the color that they want to bet in
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
                    print ("Your bet of {} to {} has been placed. We're going all in!!!".format(bet, newBet.betColor) #If player goes all in (bets all their chips)
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
        if betSlotColor(betSlot(result)) == newBet.betColor: #If player bet color was the same that the roulette got, the player wins
            bet = bet*18 if betColor == "3" else bet*2
            player1.chips = player1.chips + bet
            print("You won!!! You have won {} chips. New balance: {}".format(bet, player1.chips))
        else: 
            player1.chips = player1.chips - bet
            print("You lost :(. You have lost {} chips. New balance: {}".format(bet, player1.chips))
        if player1.chips == 0:
            break
        again = input("Do you wanna play the Roulette again? [y/n]: ") #Asking the player if they want to pay again
        while again.strip().upper() not in yesno:
            again = input("Do you wanna play the Roulette again? [y/n]: ")
        if again.strip().upper() == "YES" or again.strip().upper() == "Y":
                continue
        else:
                break
        
def blackJackGame(): #This function is the whole blackjack game.
#This function is programmed to be almost the same as a real blackjack game. In real casinos,
#blackjack payouts are rounded down if the 3:2 ratio is not payable. For example, if player bet is 5, and player has blackjack,
#the payout should be 12.5, but if 1 is the lowest chip, then the casino would round down and pay 12 instead of 13. In this program,
#that bet is rounded up. Also, program does not automatically stops when player has blackjack, and there's no insurance option.
    while True:  
        while True:    
            try:
                print ("Your chips: {}".format(player1.chips))
                bet = int(input("Please enter your bet (Bet must be a multiple of 100): ")) #This line asks the user to place a bet
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
                deck.append(letters[i]+" "+symbols2[j]) #This loop "Shuffle" the cards and create a new random deck of 52
                
        for i in range (0, 2): #This loop add 2 cards to bot dealers hand and player's hand
            addCard(deckPlayer)
            addCard(deckDealer)
        splitable = True if deckPlayer[0].split()[0] == deckPlayer[1].split()[0] else False #A player can split his hand if they got two cards with the same number. This variable will be "True" if so
        if splitable == True:
            confirmBlackjack.append("4") #This adds the option to split in applicable cases
        print("\nDealer's hand: ???", deckDealer[1]) #This prints the dealer's hand. As in real life, it only shows one of the dealer's card.
        playerBusted = False
        playerBusted2 = False
        playerBusted3 = False
        dealerBusted = False
        splitted = False
        while True: #This is the main loop for playing the game.
            playerHand.clear()
            for i in deckPlayer:
                card = cards(i.split()[0], i.split()[1])
                playerHand.append(card.val())
            if 0 in playerHand: #This condition is if the player has an Ace on their hand, and the Ace value must be changed from 11 to 1 to avoid busting.
                playerHand.append(11 if sum(playerHand)<11 else 1)
            print("\nYour hand: " + " ".join(deckPlayer))
            print(sum(playerHand))
            if sum(playerHand)>21: #If the sum of player's cards is higher than 21, then the player's hand is busted and the play is over.
                playerBusted = True
                print("\nBusted!")
                input("\nPress enter to continue.")
                break
            play = input("\n1. Stand\n2. Hit\n3. Double\n\nSelect one option [1-3]: " if splitable == False else "1. Stand\n2. Hit\n3. Double\n4. Split\nSelect one option [1-4]: ")
            while play not in confirmBlackjack:
                play = input("\n1. Stand\n2. Hit\n3. Double\n\nSelect one option [1-3]: " if splitable == False else "1. Stand\n2. Hit\n3. Double\n4. Split\nSelect one option [1-4]: ")
            #Here, the player can choose to add cards (hit), stand, double (double the bet and add 1 card), or split if applicable
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
                if player1.chips - bet < 0: #If player does not have enough chips to double, double option is not posible.
                    print("\nYou don't have enough chips to double!")
                    continue
                else:
                    player1.chips = player1.chips - bet
                    bet = 2*bet
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
                    break

            elif play == "4": #If player decides to split, two separate hands will be created for each card. (Another bet of the same amount as initial will be added to second hand)
                if player1.chips - bet < 0:
                    print("You don't have enough chips to split!")
                    input("\nPress enter to continue.")
                    continue
                else:
                    #Here, the lists have the names '2' and '3'. This does not mean that the player has 3 hands, this is done just for differentiating from initial hand list.
                    #The same logic as before will be used for each hand.
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
                    while True: #Playing first hand
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
                                bet = 2*bet
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
                                break
                    while True: #Playing second hand
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
                                bet = 2*bet
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
                    break
            
            #If player did not bust, then the dealer will play.
        if playerBusted == False and bustedSplit(playerBusted2, playerBusted3, splitted)==False:
            #The dealer is programmed using real casino's dealer rules. (A dealer must hit if below 17, must stand if 17 or above, and must hit on soft 17.)
            #Soft 17 is a 17 made by an Ace and more cards (i. e. Ace, 2 and 4 (11+2+4=17))
            while True:
                dealerHand.clear()
                for i in deckDealer:
                    card = cards(i.split()[0], i.split()[1])
                    dealerHand.append(card.val())
                if 0 in dealerHand:
                    dealerHand.append(11 if sum(dealerHand)<11 else 1)
                print("Dealer's cards: " + " ".join(deckDealer))
                print(sum(dealerHand))
                if sum(dealerHand)>21: #This will run if dealer busts.
                    dealerBusted = True
                    print("Dealer busted!")
                    input("\nPress enter to continue.")
                    break
            
                sleep(1.5)
                if sum(dealerHand)<17: #If the dealer does not have more than 17, they should hit.
                    if sum(playerHand)<sum(dealerHand): #The dealer will hit only if player has more than them.
                        break
                    else:
                        addCard(deckDealer)
                        continue
                elif sum(dealerHand)==17:   #If the dealer has 17
                    if 0 in dealerHand: #If there's a 0 in dealer's hand, that means there's an Ace. So as explained before, dealer must hit on soft 17
                        addCard(deckDealer)
                        continue
                    else:
                        break
                elif sum(dealerHand)>17: #Last condition, if dealer has more than 17
                    break
    
    
        if splitted == True: #This condition will calculate the payouts if the player splitted. This is done separately because each hand is independent.
            if dealerBusted == True: #If dealer busted, this condition will calculate the payout
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
    
            elif dealerBusted == False: #If dealer didn't bust, this condition will calculate the payout
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
                
        elif splitted == False: #If player did not split:
            if dealerBusted == True: #If dealer busted and player did not, this condition will calculate payouts
                if len(deckPlayer) == 2 and sum(playerHand) == 21:
                    print("Congrats! You have BlackJack! You win!")
                    winnings = 1.5*bet if (1.5*bet)%100 == 0 else 2*bet
                    player1.chips = player1.chips + winnings
                    print("You have won {} chips. New balance: {}".format(winnings, player1.chips))
                else:
                    print("You win!")
                    player1.chips = player1.chips + 2*bet
                    print("You won {} chips. Your new balance is: {}".format(2*bet, player1.chips))
            if playerBusted == True: #If player busted, this condition will calculate payouts (0)
                if len(deckDealer) == 2 and sum(dealerHand) == 21:
                    print("Dealer has BlackJack! You lose!")
                    print("You lost {} chips. New balance: {}".format(bet, player1.chips))
                else:
                    print("You lost!")
                    print("You lost {} chips. New balance: {}".format(bet, player1.chips))
            if playerBusted == False and dealerBusted == False: #If neither player nor dealer busted, this program will calculate payouts
                checkWinner(playerHand, bet) #calling checkWinner function
        if player1.chips > 0:#Asking the player if they wanna play again ONLY if they have more than 0 chips
            playagain = input("Wanna play BlackJack again?[y/n]: ")
            while playagain.strip().upper() not in yesno:
                playagain = input("Wanna play BlackJack again?[y/n]: ")
            if playagain.strip().upper() == "YES" or playagain.strip().upper() == "Y":
                continue
            else:
                break
        else:
            break
            
            
class cards: #Class cards, for objects type cards used in blackjack game
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
         
class player: #Class player, for the usage of this attributes in all the games
    def __init__(self, name, chips, balance):
        self.chips = chips
        self.balance = balance
        self.chips = int(self.chips)
        
class slot: #Class slot, for objects inside the roulette
    def  __init__(self, color):
        self.color = color 
        self.betColor = "Black" if self.color == "1" else "Red" if self.color == "2" else "Green"
          
print("{0:*^60}".format("Welcome to Waterloo Casino!")) #This is the finally the program run code 
sleep(1)
print("Reminder: Waterloo Casino uses special chips. The minimum value of a chip is 100")
sleep(1)
name = input("What's your name?: ")
addChips() #Adding chips to player object's balance attribute
makePayment() #Making the payment
print ("Thanks {}! Now, what would you like to play today?".format(name))
while True:
    chooseGame() #Choosing the game
    if game == "1": #Global variable "game" declared in chooseGame function
        rouletteGame()
    elif game == "2":
        blackJackGame()       
    if player1.chips==0: #When the player runs out of chips, this code block will run
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
        again = input("Do you wanna play another game? [y/n]: ") #Asking the player if they wanna play another game
        while again.strip().upper() not in yesno:
            again = input("Do you wanna play another game? [y/n]: ")
        if again.strip().upper() == "YES" or again.strip().upper() == "Y":
            continue
        else:
            print("You have cashed out ${:.2f} ({} chips).".format(player1.chips/100, player1.chips)) #Cashing out and ending program
            print("Thanks for playing at Waterloo Casino! We'll see you soon.")
            break


