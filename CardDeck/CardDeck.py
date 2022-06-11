import collections

""" 
    The first thing to note is the use of collections.namedtuple to construct a simple
    class to represent individual cards. We use namedtuple to build classes of objects that
    are just bundles of attributes with no custom methods, like a database record. In the
    example, we use it to provide a nice representation for the cards in the deck, as shown
    in the console session:
 """

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')   #Square brackets are lists
    suits = 'spades diamonds clubs hearts'.split()          #Split a string into a list 

    def __init__(self) -> None:                             #add the None annotation to always return NoneType
        self.cards = [Card(rank, suit)
            for suit in self.suits
            for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):                        #used for list indexing, dictionary lookup, or accessing ranges of values
        return self._cards[position]   
