from deck_of_cards import Card, Deck
import unittest

class CardTests(unittest.TestCase):
    
    # This "setUp" runs before each test method
    def setUp(self):
        self.card = Card("J", "Spades")
    
    # Checks to see if the card has a suit and a value
    def test_init(self):
        """Cards should have a suit and a value"""
        self.assertEqual(self.card.suit, "Spades")
        self.assertEqual(self.card.value, "J")

    # Checks to see that the representation of the card is a string
    def test_repr(self):
        """repr should return a string of the form 'VALUE of SUIT'"""
        self.assertEqual(repr(self.card), 'J of Spades')

class DeckTests(unittest.TestCase):

    # Always makes a new deck before the test cases are run
    def setUp(self):
        self.deck = Deck()

    # Checks to see that the Deck object is a list with 52 elements
    def test_init(self):
        """Decks should have a 'Cards' attribute, which is a list of values"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertTrue(len(self.deck.cards), 52)

    # Checks the representation of the Deck object
    def test_repr(self):
        """repr should return a string of the form 'Deck of COUNT cards.'"""
        self.assertEqual(repr(self.deck), "Deck of 52 cards")

    # Checks to make sure the count function returns the amount of cards in the deck
    def test_count(self):
        """Count should return a count of the number of cards in the deck"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    # Checks to make sure a specific amount of cards can be dealt
    def test_deal_sufficient_cards(self):
        """_deal should deal the number of cards specified"""
        cards = self.deck._deal(5)
        self.assertEqual(len(cards), 5)
        self.assertEqual(self.deck.count(), 47)

    # Checks to see that the maximum number of cards can be dealt
    def test_deal_insufficient_cards(self):
        """_deal should deal the number of cards left in the deck when there aren't enough to deal"""
        cards = self.deck._deal(65)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    # Checks to see that no cards are dealt when specified
    def test_deal_no_cards(self):
        """_deal should throw a value error when the deck is empty"""
        self.deck._deal(self.deck.count())
        # The "with" statement checks for errors
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    # Checks to see if a single card can be dealt from the deck
    def test_deal_card(self):
        """deal_card should deal a single card from the deck"""
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_cards()
        self.assertEqual(card, dealt_card)
        self.assertEqual(self.deck.count(), 51)

    # Checks to see if a hand can be dealt
    def test_deal_hand(self):
        """deal_hand should deal the number of cards passed in"""
        cards = self.deck.deal_hand(5)
        self.assertEqual(len(cards), 5)
        self.assertEqual(self.deck.count(), 47)

    # Checks to see if the deck can be shuffled
    def test_shuffle_deck(self):
        """shuffle should shuffle the deck if the deck is full"""
        cards = self.deck.cards[:] # The [:] is a slice that makes a copy of the deck
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)

    # Checks to make sure that a less-than-full deck cannot be shuffled
    def test_shuffle_not_full_deck(self):
        """shuffle should throw a ValueError if the deck isn't full"""
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()

# This code chunk allows the file to be run in the command line
if __name__ == '__main__':
    unittest.main()