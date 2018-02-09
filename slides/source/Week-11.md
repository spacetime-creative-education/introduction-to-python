<img src="../img/logo.jpg" width="16%" align="right">
# Inheritance, Testing


<!-- <img src="../img/hash_table.png" width="50%" align="right"> -->
---
layout: false
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Class Goals

]
.right-column[
  * Understand `Class` Inheritance
  
  * Start Test driven development

  ]
???
How are we going to do it?

By creating awesome class definitions
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Inheritance
]
.right-column[
  One of the fundamental concepts under object oriented programming, **inheritance** is the ability to define a new class that is a modified version of an existing class.

  We are gonna learn this by creating classes for *Playing cards*. After this session, you should be able to build your own card games like Poker or Rummy using inheritance and classes.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Inheritance
  ## - Card objects
]
.right-column[
  There are 52 cards in a deck, each of which belongs to one of four **suits** and one of
  thirteen **ranks**.

  The suits are Spades, Hearts, Diamonds, and Clubs. The ranks are Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King. Depending on the game that you are playing, an Ace may be higher than King or lower than 2.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Inheritance
  ## - Card objects
]
.right-column[
  The class `Card` attributes has some obvious nominees are **rank** and **suit**.

  But, what should be the `type` of these attributes?

  One possibility is using `str` like "Spade", "Hearts" etc for suits. One problem with this implementation is that it would not be easy to compare cards to see which had a higher rank or suit.
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Inheritance
  ## - Card objects
]
.right-column[
  An alternative is to use *int* to _encode_ the card ranks and suits.

  For example, Spades -> 3, Hearts -> 2, Diamonds -> 1, Clubs -> 0.
  Similarly, Ace -> 1, Jack -> 11, etc.
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Inheritance
  ## - Card objects
]
.right-column[
  Let's start with the class definition:

  ```python
  class Card(object):
      """Represents a playing card"""
      def __init__(self, suit=0, rank=2):
          self.suit = suit
          self.rank = rank

  ```
  Now you can create a card like:

  ```
  queen_of_diamonds = Card(1, 12)
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Inheritance
  ## - Card objects
]
.right-column[
  Adding class attributes

  ```python
  class Card(object):
      """Represents a playing card"""

      suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
      rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen',

      def __init__(self, suit=0, rank=2):
          self.suit = suit
          self.rank = rank

      'King']

      def __str__(self):
          return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
  ```
  Variables like `suit_names` and `rank_names` which are defined outside methods but inside a class are called `class attributes`. Where as `suit` or `rank` defined inside methods are called `instance attributes`.
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Inheritance
  ## - Card objects
]
.right-column[
  ```python
  >>> card1 = Card(2, 11)
  >>> print(card1)
  Jack of Hearts
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Inheritance
  ## - Card objects
]
.right-column[
  Comparing cards, we can override relational operators in our class to make comparison of two  cards easier. Let's override the `<` op.

  ```python
  def __lt__(self, other):
    # check the suits
    if self.suit < other.suit: return True
    if self.suit > other.suit: return False
    # suits are the same... check ranks
    return self.rank < other.rank
  ```
  This can be written more consisely using tuples.
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Inheritance
  ## - Card objects
]
.right-column[
  now that we have a Card class made, let's define a Deck of cards.

  ```python
  class Deck:
      def __init__(self):
          self.cards = []
          for suit in range(4):
              for rank in range(1, 14):
                  card = Card(suit, rank)
                  self.cards.append(card)
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Inheritance
  ## - Card objects
]
.right-column[
  now that we have a Card class made, let's define a Deck of cards.

  ```python
  class Deck:
      ...
      def __str__(self):
          res = []
          for card in self.cards:
              res.append(str(card))
          return '\n'.join(res)
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Inheritance
  ## - Card objects
]
.right-column[
  ```python
  >>> deck = Deck()
  >>> print(deck)   # will print all cards in a deck
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Inheritance
  ## - Card objects
]
.right-column[
  Deck Methods:

  To deal the cards, we need to remove or add one card at a time from/to the deck. We should also be able to shuffle the cards
  ```python
  def pop_card(self):
      return self.cards.pop()
  def add_card(self, card):
      self.cards.append(card)
  def shuffle(self):
      random.shuffle(self.cards)
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Inheritance
  ## - Card objects
]
.right-column[
  Now comes Inheritance.

  We now need a class called `Hand` that represents a subset of Deck, that any player holds in his hand. It should behave similar to Deck, but it can have more operation based on the game played.

  To say that `Hand` is inheriting from `Deck` we say

  ```python
  class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Inheritance
  ## - Card objects
]
.right-column[
  When you create a Hand, Python invokes this init method, not the one in Deck .

  ```python
  >>> hand = Hand('new hand')
  >>> hand.cards
  []
  >>> hand.label
  'new hand'
  ```
]
???
---

<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Inheritance
  ## - Card objects
]
.right-column[
  You can use the Deck method
  ```python
  >>> deck = Deck()
  >>> card = deck.pop_card()
  >>> hand.add_card(card)
  >>> print(hand)
  King of Spades
  ```
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Inheritance
  ## - Card objects
]
.right-column[
  A natural next step is to encapsulate this code in a method called move_cards :

  ```python
  def move_cards(self, hand, num):
      for i in range(num):
          hand.add_card(self.pop_card())
  ```

  move_cards takes two arguments, a Hand object and the number of cards to deal. It modifies both self and hand , and returns None .
]
???
---
<img src="../img/logo.jpg" width="16%" align="right">
.left-column[
  ## Inheritance
  ## - Card objects
]
.right-column[
  In some games, cards are moved from one hand to another, or from a hand back to the deck. You can use move_cards for any of these operations: self can be either a Deck or a Hand, and hand , despite the name, can also be a Deck.
]
???
---
