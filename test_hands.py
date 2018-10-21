import pytest
from logger import getLogger
from objects import Card, HandValue as HandVal
from session import Session

LOGGER = getLogger()

def test_high_card():
    sesh = Session(LOGGER, playerCount=2)
    players = ['Adam', 'Verina']
    for i in enumerate(players):
        sesh.players[i].name = players[i]
    sesh.setup_game()
    sesh.players[0].hand[0] = Card('H', 12)
    sesh.players[0].hand[1] = Card('S', 14)

    sesh.players[1].hand[0] = Card('C', 2)
    sesh.players[1].hand[1] = Card('D', 6)

    sesh.community_cards[0] = Card('D', 10)
    sesh.community_cards[1] = Card('S', 9)
    sesh.community_cards[2] = Card('C', 5)
    sesh.community_cards[3] = Card('D', 3)
    sesh.community_cards[4] = Card('C', 13)
    res = sesh.get_best_hands()
    assert res[sesh.players[0]][0] == HandVal.HIGH_CARD
    assert res[sesh.players[0]][1] == [Card('S', 14), Card('C', 13),
                                       Card('H', 12), Card('D', 10),
                                       Card('S', 9)]
    assert res[sesh.players[1]][0] == HandVal.HIGH_CARD
    assert res[sesh.players[1]][1] == [Card('C', 13), Card('D', 10),
                                       Card('S', 9), Card('D', 6), Card('C', 5)]



def test_full_house_pair():
    sesh = Session(LOGGER, playerCount=2)
    players = ['Adam', 'Verina']
    for i in enumerate(players):
        sesh.players[i].name = players[i]
    sesh.setup_game()
    sesh.players[0].hand[0] = Card('H', 12)
    sesh.players[0].hand[1] = Card('S', 12)
    sesh.players[1].hand[0] = Card('C', 10)
    sesh.players[1].hand[1] = Card('D', 8)
    sesh.community_cards[0] = Card('D', 10)
    sesh.community_cards[1] = Card('S', 10)
    sesh.community_cards[2] = Card('C', 8)
    sesh.community_cards[3] = Card('D', 7)
    sesh.community_cards[4] = Card('C', 12)
    res = sesh.get_best_hands()
    assert res[sesh.players[0]][0] == HandVal.FULL_HOUSE
    assert res[sesh.players[1]][0] == HandVal.FULL_HOUSE

def test_full_house2():
    sesh = Session(LOGGER, playerCount=2)
    players = ['Adam', 'Verina']
    for i in enumerate(players):
        sesh.players[i].name = players[i]
    sesh.setup_game()
    sesh.players[0].hand[0] = Card('H', 12)
    sesh.players[0].hand[1] = Card('C', 10)

    sesh.players[1].hand[0] = Card('H', 10)
    sesh.players[1].hand[1] = Card('D', 8)

    sesh.community_cards[0] = Card('D', 10)
    sesh.community_cards[1] = Card('S', 10)
    sesh.community_cards[2] = Card('C', 8)
    sesh.community_cards[3] = Card('D', 7)
    sesh.community_cards[4] = Card('C', 12)
    res = sesh.get_best_hands()
    assert res[sesh.players[0]][0] == HandVal.FULL_HOUSE
    assert res[sesh.players[0]][1][0] == 10
    assert res[sesh.players[0]][1][1] == 12
    assert res[sesh.players[1]][0] == HandVal.FULL_HOUSE
    assert res[sesh.players[1]][1][0] == 10
    assert res[sesh.players[1]][1][1] == 8

def test_full_house3():
    sesh = Session(LOGGER, playerCount=2)
    players = ['Adam', 'Verina']
    for i in enumerate(players):
        sesh.players[i].name = players[i]
    sesh.setup_game()
    sesh.players[0].hand[0] = Card('H', 12)
    sesh.players[0].hand[1] = Card('C', 10)
    sesh.players[1].hand[0] = Card('H', 10)
    sesh.players[1].hand[1] = Card('D', 8)
    sesh.community_cards[0] = Card('D', 12)
    sesh.community_cards[1] = Card('S', 10)
    sesh.community_cards[2] = Card('C', 8)
    sesh.community_cards[3] = Card('S', 8)
    sesh.community_cards[4] = Card('C', 12)
    res = sesh.get_best_hands()
    assert res[sesh.players[0]][0] == HandVal.FULL_HOUSE
    assert res[sesh.players[0]][1][0] == 12
    assert res[sesh.players[0]][1][1] == 10
    assert res[sesh.players[1]][0] == HandVal.FULL_HOUSE
    assert res[sesh.players[1]][1][0] == 8
    assert res[sesh.players[1]][1][1] == 10

def test_pockets():
    sesh = Session(LOGGER, playerCount=2)
    players = ['Adam', 'Verina']
    for i in enumerate(players):
        sesh.players[i].name = players[i]
    sesh.setup_game()
    sesh.players[0].hand[0] = Card('H', 12)
    sesh.players[0].hand[1] = Card('S', 12)
    sesh.players[1].hand[0] = Card('C', 10)
    sesh.players[1].hand[1] = Card('S', 10)
    sesh.community_cards[0] = Card('H', 9)
    sesh.community_cards[1] = Card('S', 4)
    sesh.community_cards[2] = Card('C', 8)
    sesh.community_cards[3] = Card('D', 7)
    sesh.community_cards[4] = Card('C', 13)
    res = sesh.get_best_hands()
    assert res[sesh.players[0]][0] == HandVal.PAIR
    assert res
    assert res[sesh.players[1]][0] == HandVal.PAIR

def test_flush_1():
    sesh = Session(LOGGER, playerCount=2)
    players = ['Adam', 'Verina']
    for i in enumerate(players):
        sesh.players[i].name = players[i]
    sesh.setup_game()
    sesh.players[0].hand[0] = Card('H', 12)
    sesh.players[0].hand[1] = Card('S', 13)
    sesh.players[1].hand[0] = Card('D', 10)
    sesh.players[1].hand[1] = Card('D', 8)

    sesh.community_cards[0] = Card('H', 10)
    sesh.community_cards[1] = Card('C', 10)
    sesh.community_cards[2] = Card('D', 5)
    sesh.community_cards[3] = Card('D', 7)
    sesh.community_cards[4] = Card('D', 12)
    res = sesh.get_best_hands()
    assert res[sesh.players[0]][0] == HandVal.TWO_PAIR
    # assert res[sesh.players[0]][1][0] == 12
    # assert res[sesh.players[0]][1][1] == 12
    # assert res[sesh.players[0]][1][2] == 10
    # assert res[sesh.players[0]][1][3] == 10
    # assert res[sesh.players[0]][1][4] == 13
    assert res[sesh.players[1]][0] == HandVal.FLUSH
    assert res[sesh.players[1]][1][0] == 12
    assert res[sesh.players[1]][1][1] == 10
    assert res[sesh.players[1]][1][2] == 8
    assert res[sesh.players[1]][1][3] == 7
    assert res[sesh.players[1]][1][4] == 5

def test_straight_1():
    sesh = Session(LOGGER, playerCount=2)
    players = ['Adam', 'Verina']
    for i in enumerate(players):
        sesh.players[i].name = players[i]
    sesh.setup_game()
    sesh.players[0].hand[0] = Card('S', 12)
    sesh.players[0].hand[1] = Card('C', 11)
    sesh.players[1].hand[0] = Card('D', 10)
    sesh.players[1].hand[1] = Card('D', 8)
    sesh.community_cards[0] = Card('S', 10)
    sesh.community_cards[1] = Card('D', 9)
    sesh.community_cards[2] = Card('C', 8)
    sesh.community_cards[3] = Card('D', 7)
    sesh.community_cards[4] = Card('C', 12)
    res = sesh.get_best_hands()
    assert res[sesh.players[0]][0] == HandVal.STRAIGHT
    assert res[sesh.players[0]][1][0] == 12
    assert res[sesh.players[0]][1][1] == 11
    assert res[sesh.players[0]][1][2] == 10
    assert res[sesh.players[0]][1][3] == 9
    assert res[sesh.players[0]][1][4] == 8
    assert res[sesh.players[1]][0] == HandVal.TWO_PAIR

def test_ace_high_straight():
    sesh = Session(LOGGER, playerCount=2)
    players = ['Adam', 'Verina']
    for i in enumerate(players):
        sesh.players[i].name = players[i]
    sesh.setup_game()
    sesh.players[0].hand[0] = Card('S', 14)
    sesh.players[0].hand[1] = Card('C', 2)
    sesh.players[1].hand[0] = Card('D', 10)
    sesh.players[1].hand[1] = Card('D', 8)
    sesh.community_cards[0] = Card('S', 13)
    sesh.community_cards[1] = Card('D', 12)
    sesh.community_cards[2] = Card('C', 11)
    sesh.community_cards[3] = Card('D', 7)
    sesh.community_cards[4] = Card('C', 10)
    res = sesh.get_best_hands()
    assert res[sesh.players[0]][0] == HandVal.STRAIGHT
    for i in reversed(range(10, 15)):
        assert res[sesh.players[0]][1][14 - i] == i
    assert res[sesh.players[1]][0] == HandVal.PAIR

def test_ace_low_straight():
    sesh = Session(LOGGER, playerCount=2)
    players = ['Adam', 'Verina']
    for i in enumerate(players):
        sesh.players[i].name = players[i]
    sesh.setup_game()
    sesh.players[0].hand[0] = Card('S', 14)
    sesh.players[0].hand[1] = Card('C', 2)
    sesh.players[1].hand[0] = Card('D', 10)
    sesh.players[1].hand[1] = Card('D', 8)
    sesh.community_cards[0] = Card('S', 3)
    sesh.community_cards[1] = Card('D', 4)
    sesh.community_cards[2] = Card('C', 5)
    sesh.community_cards[3] = Card('D', 9)
    sesh.community_cards[4] = Card('C', 10)
    res = sesh.get_best_hands()
    assert res[sesh.players[0]][0] == HandVal.STRAIGHT
    for i in reversed(range(2, 6)):
        assert res[sesh.players[0]][1][5 - i] == i
    assert res[sesh.players[0]][1][-1] == 1 #ace
    assert res[sesh.players[1]][0] == HandVal.PAIR

def test_straight_flush_1():
    sesh = Session(LOGGER, playerCount=2)
    players = ['Adam', 'Verina']
    for i in enumerate(players):
        sesh.players[i].name = players[i]
    sesh.setup_game()
    sesh.players[0].hand[0] = Card('S', 14)
    sesh.players[0].hand[1] = Card('S', 2)
    sesh.players[1].hand[0] = Card('D', 10)
    sesh.players[1].hand[1] = Card('D', 8)
    sesh.community_cards[0] = Card('S', 3)
    sesh.community_cards[1] = Card('S', 4)
    sesh.community_cards[2] = Card('S', 5)
    sesh.community_cards[3] = Card('D', 6)
    sesh.community_cards[4] = Card('C', 10)
    res = sesh.get_best_hands()
    assert res[sesh.players[0]][0] == HandVal.STRAIGHT_FLUSH
    for i in reversed(range(2, 6)):
        assert res[sesh.players[0]][1][5 - i] == i
    assert res[sesh.players[0]][1][-1] == 1
    assert res[sesh.players[1]][0] == HandVal.PAIR

def test_straight_flush_2():
    sesh = Session(LOGGER, playerCount=2)
    players = ['Adam', 'Verina']
    for i in enumerate(players):
        sesh.players[i].name = players[i]
    sesh.setup_game()
    sesh.players[0].hand[0] = Card('D', 10)
    sesh.players[0].hand[1] = Card('D', 8)
    sesh.players[1].hand[0] = Card('C', 6)
    sesh.players[1].hand[1] = Card('C', 2)
    sesh.community_cards[0] = Card('C', 3)
    sesh.community_cards[1] = Card('C', 4)
    sesh.community_cards[2] = Card('C', 5)
    sesh.community_cards[3] = Card('D', 7)
    sesh.community_cards[4] = Card('C', 10)
    res = sesh.get_best_hands()
    assert res[sesh.players[0]][0] == HandVal.PAIR
    assert res[sesh.players[1]][0] == HandVal.STRAIGHT_FLUSH
    for i in reversed(range(2, 7)):
        assert res[sesh.players[1]][1][6 - i] == i

def test_royal_flush_1():
    sesh = Session(LOGGER, playerCount=2)
    players = ['Adam', 'Verina']
    for i in enumerate(players):
        sesh.players[i].name = players[i]
    sesh.setup_game()
    sesh.players[0].hand[0] = Card('D', 10)
    sesh.players[0].hand[1] = Card('D', 12)
    sesh.players[1].hand[0] = Card('C', 6)
    sesh.players[1].hand[1] = Card('C', 2)

    sesh.community_cards[0] = Card('D', 14)
    sesh.community_cards[1] = Card('D', 11)
    sesh.community_cards[2] = Card('D', 2)
    sesh.community_cards[3] = Card('D', 7)
    sesh.community_cards[4] = Card('D', 13)
    res = sesh.get_best_hands()
    assert res[sesh.players[0]][0] == HandVal.ROYAL_FLUSH
    for i in reversed(range(10, 15)):
        assert res[sesh.players[0]][1][14 - i] == i
    assert res[sesh.players[1]][0] == HandVal.FLUSH
    for i in reversed(range(10, 15)):
        assert res[sesh.players[0]][1][14 - i] == i

def test_royal_flush_2():
    sesh = Session(LOGGER, playerCount=2)
    players = ['Adam', 'Verina']
    for i in enumerate(players):
        sesh.players[i].name = players[i]
    sesh.setup_game()
    sesh.players[0].hand[0] = Card('D', 10)
    sesh.players[0].hand[1] = Card('D', 12)
    sesh.players[1].hand[0] = Card('C', 8)
    sesh.players[1].hand[1] = Card('C', 2)
    sesh.community_cards[0] = Card('D', 14)
    sesh.community_cards[1] = Card('D', 11)
    sesh.community_cards[2] = Card('C', 10)
    sesh.community_cards[3] = Card('D', 7)
    sesh.community_cards[4] = Card('D', 13)
    res = sesh.get_best_hands()
    assert res[sesh.players[0]][0] == HandVal.ROYAL_FLUSH
    assert res[sesh.players[1]][0] == HandVal.HIGH_CARD

if __name__ == '__main__':
    # test_full_house2()
    pytest.main(['test_hands.py'])