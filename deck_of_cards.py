# Import statements
from random import shuffle

# Defines the Card class
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:

    # Initializes the deck
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        # Uses list comprehension
        self.cards = [Card(value, suit) for suit in suits for value in values]

    # Returns the number of cards in the deck in the form of a string
    def __repr__(self):
        return f"Deck of {self.count()} cards"

    # Iterates over the deck of cards using an iterator
    def __iter__(self):
        return iter(self.cards)

    # Gets the amount of cards in the deck
    def count(self):
        return len(self.cards)

    # num = the number of cards we want to remove
    def _deal(self, num):
        count = self.count()
        actualNumberToRemove = min([count, num])

        # Accounts for a deck of zero cards
        if count == 0:
            raise ValueError("All cards have already been dealt!")
        # Go "actualNumberToRemove" spaces back and remove the cards from there through the end
        cards = self.cards[-actualNumberToRemove:]
        # Redefines self.cards to omit the cards that were dealt
        self.cards = self.cards[:-actualNumberToRemove]
        return cards

    def deal_cards(self):
        # Returns a SINGLE card, not a card from a list
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled!")
        # Shuffle method from above is implemented here
        shuffle(self.cards)
        return self
    
# Tests...
deck = Deck()
deck.shuffle()

# Iterates over the list of cards, printing each one out
# Utilizes the __iter__ function above
for card in deck:
    print(card)