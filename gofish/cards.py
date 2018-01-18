import random
#from gofish import extras
import extras

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.sets = []


def take_cards(asking_player, giving_player, card=None):

    # takes from the main deck
    if card == None:
        asking_player.hand.append(giving_player[0])
        giving_player.remove(giving_player[0])

    # takes from another player
    elif card != None:
        total = giving_player.hand.count(card)

        for _ in range(total):
            asking_player.hand.append(card)
            giving_player.hand.remove(card)


def create_deck():
    deck = []

    for _ in range(4):
        for i in extras.types:
            deck.append(i)

    random.shuffle(deck)
    return deck
