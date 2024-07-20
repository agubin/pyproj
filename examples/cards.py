import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    rank = [str(n) for n in range(2,11)] + list('JQKA')
    suit = 'spades diamonds clubs hearts'.split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self._cards = [Card(r, s) for s in self.suit for r in self.rank]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]