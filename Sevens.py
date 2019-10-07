import Standard, random, math

hand = []
pos = False
numberOfPlayers = 0
sevens = [[],[],[],[]]
Hearts = []
Diamonds = []
Clubs = []
Spades = []

#adds a card to the start of the suit
def addToStartSuit(card):
    if card[0] == 'H':
        Hearts.insert(0,card)        
    elif card[0] == 'D':
        Diamonds.insert(0,card)
    elif card[0] == 'C':
        Clubs.insert(0,card)    
    elif card[0] == 'S':
       Spades.insert(0,card)

#adds a card to the end of the suit
def addToEndSuit(card):
    if card[0] == 'H':
        Hearts.append(card)        
    elif card[0] == 'D':
        Diamonds.append(card)
    elif card[0] == 'C':
        Clubs.append(card)    
    elif card[0] == 'S':
       Spades.append(card)

#adds all 7's to the sevens list            
def addSuitSevens(card):
    hasBeenAdded = False
    for seven in sevens:
        if len(seven) == 0 and not hasBeenAdded:
            seven.append(card)
            hasBeenAdded = True

#checks to see what player goes first
def playFirstSeven(hands):
    result = -1
    firstCardToPlay = "S7"
    for counter in range(0, len(hands)):
        if firstCardToPlay in hands[counter]:
            result = counter
            Standard.playACard(hands[counter],firstCardToPlay)
            addToStartSuit(firstCardToPlay)
            addSuitSevens(firstCardToPlay)

    return result

#Checks if they have a 7 to play
def canPlaySeven(card, hand):
    result = False
    if card in hand:
        if card[1] == '7':
            result = True
    
    return result

#checks to see if a player can play a card
def canPlayCard(card, hand):
    global pos
    pos = False
    result = False
    Standard.convertFacesToNumbers(hand)
    if card in hand:
        if card[0] == 'H':
            for h in range(len(Hearts)):
                if int(Hearts[h][1:3])-1 == int(card[1:3]):
                    result = True
                    pos = True
                    pos = int(h+1)
                elif int(Hearts[h-1][1:3])+1 == int(card[1:3]):
                    result = True
                    pos = False
        elif card[0] == 'D':
            for d in range(len(Diamonds)):
                if int(Diamonds[d][1:3])-1 == int(card[1:3]):
                    result = True
                    pos = True
                elif int(Diamonds[d-1][1:3])+1 == int(card[1:3]):
                    result = True
                    pos = False
        elif card[0] == 'C':
            for c in range(len(Clubs)):
                if int(Clubs[c][1:3])-1 == int(card[1:3]):
                    result = True
                    pos = True
                elif int(Clubs[c-1][1:3])+1 == int(card[1:3]):
                    result = True
                    pos = False
        elif card[0] == 'S':
            for s in range(len(Spades)):
                if int(Spades[s][1:3])-1 == int(card[1:3]):
                    result = True
                    pos = True
                elif int(Spades[s-1][1:3])+1 == int(card[1:3]):
                    result = True
                    pos = False

    return result

#Checks if someone has one
def findWinner(hands):
    won = False

    for players in range(0, numberOfPlayers):
        if  len(hands[players]) == 0:
            print('Player ', int(players)+1, ' is the winner!!')
            won = True
    
    return won


#allows the user to select and play a card
def play(hands, deck):

    global hand
    player = playFirstSeven(hands)
    print(player)
    print(hands)
    print(sevens)
    print(Hearts)
    print(Diamonds)
    print(Clubs)
    print(Spades)

    while findWinner(hands) == False:

        for players in range(0, numberOfPlayers):
            print('Player:', int(players)+1)
            print(hands[players])
            hand = hands[players]

            cardToPlay = input('Please enter the card you would like to play. ')
            cardToPlay = cardToPlay.upper()

            if canPlaySeven(cardToPlay, hand):
                print("You have a seven")
                addSuitSevens(cardToPlay)
                addToStartSuit(cardToPlay)
                Standard.playACard(hands[players], cardToPlay)

            elif canPlayCard(cardToPlay, hand):
                if pos == True:
                    addToStartSuit(cardToPlay)
                elif pos == False:
                    addToEndSuit(cardToPlay)
                Standard.playACard(hands[players], cardToPlay)

            else:
                print("You cannot play that card!")
                
            print(sevens)            
            print(Hearts)
            print(Diamonds)
            print(Clubs)
            print(Spades)
            findWinner(hands)



#runs the program
def main():
    global numberOfPlayers
    numberOfPlayers = int(input('Please enter the number of players (minimum of 3). '))
    while numberOfPlayers < 3:
        numberOfPlayers = int(input('Number of players must be greater than 2. '))

    deck = Standard.generateDeck()
    deck = Standard.shuffleCards(deck)
    hands = Standard.dealCards(deck,0, numberOfPlayers, [])
    play(hands, deck)

main()