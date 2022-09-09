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



"""if Ace:
    default = 11
    if total > 21:
        total -= 10
"""

class Deck:
    def __init__(self):
        SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        VALUES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        Count = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.cards = deque()
        for suit in SUITS:
            for value in VALUES:
                self.cards.append(Card(suit, value))

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
    def __init__(self, cards):
        self.cards = cards


    def add(self, card):
        self.card.append(card)


class BlackJack:
    def __init__(self, numOfPlayers):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = deque()
        self.dealer = deque()

        self.players = [Player() for x in range(numOfPlayers)]

    def _get_score(self):
        player_score = 0
        dealer_score = 0
        for card in self.player:
            if card.value == 'Ace':
                player_score += 11
            elif card.value in ['Jack', 'Queen', 'King']:
                player_score += 10
            else:
                player_score += card.count()

        for card in self.dealer:
            if card.value == 'Ace':
                dealer_score += 11
            elif card.value in ['Jack', 'Queen', 'King']:
                dealer_score += 10
            else:
                dealer_score += card.count()

        return player_score, dealer_score


    def _print_current_hand(self):
        print("Player's hand:")
        for card in self.player:
            print(card)

        print("Dealer's hand:")
        for card in self.dealer:
            print(card)

    def deal_new_hand(self, numPlayers):
        for x in range(numPlayers):
            self.player.append(self.deck.draw())
            self.player.append(self.deck.draw())
        self.dealer.append(self.deck.draw())
        self.dealer.append(self.deck.draw())


    
    def hit(self):
        if self.deck.size() > 0:
            #self.player.append(self.deck.draw())
            
            myPlayer.add(self.deck.draw)
            self._print_current_hand()
            self._get_score()

        else:
            raise Exception("Deck is empty")

    def reshuffle(self):
        self.deck.reset()
        self.player = deque()
        self.dealer = deque()

myGame = BlackJack()

myGame.deal_new_hand()

myGame.hit()

    
