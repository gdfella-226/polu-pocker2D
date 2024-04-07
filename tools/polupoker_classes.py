from random import shuffle, randint
import pygame
from time import sleep


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
    def getsuit(self):
        return self.suit
    def getval(self):
        return self.val


class Deck:
    def __init__(self, cards:list, bank, player, ai):
        self.cards = cards
        shuffle(self.cards)
        self.d_cards = self.inst(5)
        self.bank = bank
        self.player = player
        self.ai = ai


    def inst(self, n):
        out = []
        for i in n:
            out.append(self.cards.pop(randint(0, len(self.cards)-1)))
        return out

    def deck_gen(self, s, v, p):
        out = []
        for i in d_cards:
            g = int(s.index(i.suit))
            h = int(v.index(i.val))
            out.append(p[g][h])
        print(out)
        return out


    def get_cards(self):
        return self.cards


class Player:
    def __init__(self, bank, deck):
        self.deck = deck
        self.cards = self.deck.inst(2)
    def pASS(self):
        self.cards = []


class AI:
    def __init__(self, bank, deck:Deck):
        self.cards = deck.inst(2)
        self.bank = bank
        self.deck = deck
    def checkdeck(self):
        self.deckcards = self.deck.get_cards()
        for i in self.deckcards:
            print('jopa')


class Handler():
    def __init__(self):
        self.suits = ['Крести', 'Буби', 'Черви', 'Пики']
        self.vals = ['2', '3', '4', '5', '6', '7',
                     '8', '9', '10', 'В', 'Д', 'К', 'Т']
        self.pics = [['2_of_clubs.png', '3_of_clubs.png', '4_of_clubs.png', '5_of_clubs.png',
                      '6_of_clubs.png', '7_of_clubs.png', '8_of_clubs.png', '9_of_clubs.png',
                      '10_of_clubs.png', 'jack_of_clubs2.png', 'queen_of_clubs2.png', 'king_of_clubs2.png',
                      'ace_of_clubs.png'],
                     ['2_of_diamonds.png', '3_of_diamonds.png', '4_of_diamonds.png', '5_of_diamonds.png',
                      '6_of_diamonds.png', '7_of_diamonds.png', '8_of_diamonds.png', '9_of_diamonds.png',
                      '10_of_diamonds.png', 'jack_of_diamonds2.png', 'queen_of_diamonds2.png', 'king_of_diamonds2.png',
                      'ace_of_diamonds.png'],
                     ['2_of_hearts.png', '3_of_hearts.png', '4_of_hearts.png', '5_of_hearts.png',
                      '6_of_hearts.png', '7_of_hearts.png', '8_of_hearts.png', '9_of_hearts.png',
                      '10_of_hearts.png', 'jack_of_hearts2.png', 'queen_of_hearts2.png', 'king_of_hearts2.png',
                      'ace_of_hearts.png', ],
                     ['2_of_spades.png', '3_of_spades.png', '4_of_spades.png', '5_of_spades.png',
                      '6_of_spades.png', '7_of_spades.png', '8_of_spades.png', '9_of_spades.png',
                      '10_of_spades.png', 'jack_of_spades2.png', 'queen_of_spades2.png', 'king_of_spades2.png',
                      'ace_of_spades2.png']
                     ]

    def operate(self, cards, pics):
        out = []
        for i in cards:
            out.append(pics[self.suits.index(i.getsuit())]
                       [self.vals.index(i.getval())])
        return out
