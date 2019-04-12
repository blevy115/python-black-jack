import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        deck_string = ''
        for card in self.deck:
            deck_string += '\n' + card.__str__()
        return decl_string

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        card = self.deck.pop(0)
        return card

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self,deck):
        card = deck.deal()
        self.cards.append(card)
        self.value += values[self.cards[-1].rank]
        if self.value > 21:
            self.adjust_for_ace()

    def adjust_for_ace(self):
        for card in self.cards:
            if card.rank == 'Ace':
                self.value -= 10


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet():
    while True:
        try:
            bet = int(input('Please enter wager '))
        except:
            print('Please enter a valid bet')
        else:
            return bet
            break


def hit(deck,hand):
    hand.add_cards(deck)

def hit_or_stand(deck,hand):
    global playing
    choice = input('Hit or Stand ').lower()
    if choice == 'hit':
        hit(deck,hand)
    elif choice == 'stand':
        playing = False
    else:
        print('Please enter valid choice')
        hit_or_stand(deck,hand)


def show_some(player, dealer):
    print('Your cards')
    for card in player.cards:
        print(card)

    print('Dealers Card')
    print(dealer.cards[1])

def show_all(player, dealer):
    print('Your cards')
    for card in player.cards:
        print(card)

    print('Dealers Cards')
    for card in dealer.cards:
        print(card)

def player_busts(chips):
    print('Player has lost')
    chips.lose_bet()

def player_wins(chips):
    print('Player has won')
    chips.win_bet()

def dealer_busts(chips):
    print('Dealer has lost')
    chips.win_bet()


def dealer_wins(chips):
    print('Dealer has won')
    chips.lose_bet()

while True:
    print('Welcome to Black Jack')
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_cards(deck)
    dealer_hand.add_cards(deck)
    player_hand.add_cards(deck)
    dealer_hand.add_cards(deck)
    try:
        player_chips
    except:
        player_chips = Chips()
    player_chips.bet = take_bet()
    while player_chips.bet > player_chips.total:
        print('Bet exceeds total')
        player_chips.bet = take_bet()
    show_some(player_hand, dealer_hand)
    playing = True
    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)
        if player_hand.value > 21:
            player_busts(player_chips)
            break
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        show_all(player_hand, dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_chips)
        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_chips)

    print(f'You now have {player_chips.total} chips')
    choice = input('Play again (y/n)')
    if choice == 'n':
        print('Good Playing')
        break
