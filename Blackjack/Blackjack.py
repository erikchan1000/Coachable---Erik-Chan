import random
from collections import deque

class Card:
    def __init__(self, suit, value, count):
        self.suit = suit
        self.value = value
        self.count = count

    def suit(self):
        return self.suit

    def value(self):
        return self.value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def count(self):
        return self.count

class Deck:
    def __init__(self):
        SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        VALUES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        Count = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.cards = deque()
        for suit in SUITS:
            for value in range(len(VALUES)):
                self.cards.append(Card(suit, VALUES[value], Count[value]))

    def size(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def peek(self):
        return self.cards[0]

    def draw(self):
        return self.cards.popleft()

    def add_card(self, card):
        if self.size() < 52:
            self.cards.append(card)

        else:
            raise Exception("Deck is full")

    def print_deck(self):
        for card in self.cards:
            print(card)

    def reset(self):
        SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        VALUES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        self.cards = deque()
        for suit in SUITS:
            for value in VALUES:
                self.cards.append(Card(suit, value))

        self.shuffle()

class Player:
    def __init__(self):
        self.cards = deque()


    def add(self, card):
        self.cards.append(card)

    def getCards(self):
        return self.cards

    def reset(self):
        self.cards = deque()

    def length(self):
        return len(self.cards)


class BlackJack:
    def __init__(self, numOfPlayers = 1):
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = deque()
        self.players = []

        for x in range(numOfPlayers):
            self.players.append(Player())

    def getAll(self):
        for x in range(len(self.players)):
            dealer = self._get_score()[1]
            player = self._get_score(x)[0]

            print(f"Dealer: {dealer}")
            print(f"Player {x}: {player}")

        print("\n")

    def _get_score(self, playerNum = 0):
        player_score = 0
        dealer_score = 0

        playerAces = 0
        dealerAces = 0 

        for card in self.players[playerNum].getCards():
            if card.value == 'Ace':
                playerAces += 1

            player_score += card.count

            if player_score > 21 and playerAces:
                player_score -= 10
                playerAces -= 1

        for card in self.dealer:
            if card.value == 'Ace':
                dealerAces += 1

            dealer_score += card.count

            if dealer_score > 21 and dealerAces:
                dealer_score -= 10
                dealerAces -= 1

        return player_score, dealer_score

    def getResults(self):
        dealerScore = self._get_score()[0]

        print(f"Dealer Sccore: {dealerScore}")
        for x in range(len(self.players)):
            playerScore = self._get_score(x)[1]

            if playerScore > 21:
                playerScore = "Busted"

            elif playerScore == 21 and self.players[x].length() == 2:
                playerScore = "Blackjack!"

            print(f"Player {x} Score: {playerScore}")

        print("\n")


    def _print_current_hand(self, num = 0):
        print(f"Player {num} hand:")
        for card in self.players[num].getCards():
            print(card)

        print("Dealer's hand:")
        for card in self.dealer:
            print(card)

        print("\n")

    def deal_new_hand(self):
        for x in range(len(self.players)):
            self.players[x].add(self.deck.draw())
            self.players[x].add(self.deck.draw())
        
        self.dealer.append(self.deck.draw())
        self.dealer.append(self.deck.draw())


    
    def hit(self, playerNum = 0):
        if self.deck.size() > 0:
            self.players[playerNum].add(self.deck.draw())
            self._print_current_hand(playerNum)
            self._get_score(playerNum)

            if self._get_score(playerNum)[0] == 21 and self.players[playerNum].length() == 2:
                print(f"BlackJack! Player {playerNum} wins 3/2")

            if self._get_score(playerNum)[0] > 21:
                print(f"Player {playerNum} Busts.")

        else:
            raise Exception("Deck is empty")

        print("\n")

    def dealerHit(self):
        if self.deck.size() > 0:
            self.dealer.append(self.deck.draw())

    def Pass(self, playerNum = 0):
        while self._get_score()[1] < 17:
            self.dealerHit()

        print(self._get_score()[1])

        if self._get_score()[1] > 21:
            print("Dealer Bust, Player Wins")

        print("\n")

    def reshuffle(self):
        self.deck.reset()
        for x in self.players:
            x.reset()

        self.dealer = deque()

myGame = BlackJack(4)

myGame.deal_new_hand()

myGame.getAll()

myGame.hit()

myGame._print_current_hand(1)

myGame._print_current_hand(3)