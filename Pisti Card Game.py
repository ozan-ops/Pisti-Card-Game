# Importing random module and defining card suits and ranks
import random

# Card creation
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

# Card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.suit} {self.rank}"

# Deck class
class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.all_cards.append(card)

    # Shuffle the deck
    def shuffle(self):
        random.shuffle(self.all_cards)

    # Deal a card from the deck
    def deal_card(self):
        return self.all_cards.pop()

    # Print the deck
    def __str__(self):
        complete_cards = ''
        for card in self.all_cards:
            complete_cards += "\n" + card.__str__()
        return complete_cards

# Player class
class Player:
    def __init__(self):
        self.hand = []

    # Play a card
    def play_card(self, response):
        for card in self.hand:
            if response == card.__str__():
                self.hand.remove(card)
                return card
        return None

# Class for cards in the middle
class MiddlePile:
    def __init__(self):
        self.middle_cards = []

    def add_card(self, card):
        self.middle_cards.append(card)

# Class for cards won by players
class CapturedCards:
    def __init__(self):
        self.captured = []

    # Add captured cards
    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.captured.extend(new_cards)
        else:
            self.captured.append(new_cards)

# Deal cards to players and middle pile
def deal_cards(lst, deck):
    for _ in range(10):
        card = deck.deal_card()
        lst.append(card)

# Show cards
def show_cards(lst):
    card_list = [str(card) for card in lst]
    print(card_list)

# Check if the deck is almost empty
def check_end_game(deck, player1_list, player2_list):
    if 0 <= len(deck) <= 4:
        if len(player1_list) > len(player2_list):
            print("PLAYER 1 WINS!!")
        elif len(player1_list) < len(player2_list):
            print("PLAYER 2 WINS!!")
        else:
            print("IT'S A TIE")
        return True
    return False

# Play a card to the middle pile
def play_to_middle(player, middle_pile):
    while True:
        response = input("Enter the card you want to play (e.g., Hearts Two): ")
        card = player.play_card(response)
        if card is not None:
            middle_pile.add_card(card)
            break
        else:
            print("You must enter a valid card. Please try again.")

# Determine who starts first
def determine_first_player():
    number = random.randint(1, 2)
    if number == 1:
        print("Player One starts")
        return True
    else:
        print("Player Two starts")
        return False

# Check if a player captures cards
def check_capture(middle_pile, player):
    if len(middle_pile.middle_cards) >= 2:
        last_card = middle_pile.middle_cards[-1]
        last_card_value = values[last_card.rank]
        second_last_card = middle_pile.middle_cards[-2]
        second_last_card_value = values[second_last_card.rank]

        if last_card_value == second_last_card_value:
            player.add_cards(middle_pile.middle_cards)
            middle_pile.middle_cards.clear()

# Main game loop
while True:
    print("WELCOME TO PİŞTİ CARD GAME!!!")
    # Create and shuffle the deck
    deck = Deck()
    deck.shuffle()

    # Create player hands and middle pile
    player1 = Player()
    player2 = Player()
    middle_pile = MiddlePile()

    # Create classes for players' captured cards
    player1_captured = CapturedCards()
    player2_captured = CapturedCards()

    # Deal cards to players and middle pile
    deal_cards(player1.hand, deck)
    deal_cards(player2.hand, deck)
    deal_cards(middle_pile.middle_cards, deck)

    # Determine who starts first
    first_player = determine_first_player()

    # Game loop
    game = True
    while game:
        print("Cards in the middle: ")
        show_cards(middle_pile.middle_cards)
        print("\n")

        if len(player1.hand) == 0:
            deal_cards(player1.hand, deck)

        if len(player2.hand) == 0:
            deal_cards(player2.hand, deck)

        if first_player:
            print("Player One's cards: ")
            show_cards(player1.hand)
            print("\n")
            play_to_middle(player1, middle_pile)
            check_capture(middle_pile, player1_captured)
            print("Player One's captured cards: ")
            show_cards(player1_captured.captured)

            if check_end_game(deck.all_cards, player1_captured.captured, player2_captured.captured):
                game = False

            first_player = False

        else:
            print("Player Two's cards: ")
            show_cards(player2.hand)
            print("\n")
            play_to_middle(player2, middle_pile)
            check_capture(middle_pile, player2_captured)
            print("Player Two's captured cards: ")
            show_cards(player2_captured.captured)
            print("Deck length: ", len(deck.all_cards))
            if check_end_game(deck.all_cards, player1_captured.captured, player2_captured.captured):
                game = False

            first_player = True

    replay = input("Do you want to play again? (Type 'yes' or 'y' for Yes, 'no' or 'n' for No): ").lower()
    if replay in ['yes', 'y']:
        continue
    else:
        print("Good day!")
        break
