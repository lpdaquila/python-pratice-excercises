from collections import namedtuple

Card = namedtuple('Card', ['value', 'symbol'])

king_spade = Card('K', '♠️')

print(king_spade)
print(king_spade._asdict())
print(king_spade.symbol)
print(king_spade.value)