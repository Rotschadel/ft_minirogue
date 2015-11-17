from Level import *
import curses
from Room import *

class Personnage (object):

    def __init__(self, nom, health, level, exp, attack, defense, wealth, x, y, player=False):
        self.name = nom
        self.hp = health
        self.lvl = level
        self.xp = exp
        self.strength = attack
        self.armour = defense
        self.gold = wealth
        self.abs = x
        self.ord = y
        self.isPlayer = player
        self.room = None

    def isHit(self, power):
        self.hp -= power

    def isDead(self):
        return self.hp < 0

    def hits(self, perso):
        if perso.lvl.defense + perso.armour - self.strength - self.lvl.attack < 0 :
            perso.hp -= self.strength + self.lvl.attack - perso.lvl.defense - perso.armour


    def moves(self, dir, r):
        x = {'l': -1, 'r': 1, 'u': 0, 'd': 0}[dir]
        y = {'d': -1, 'u': 1, 'l': 0, 'r': 0}[dir]
        if self.abs + x > 0 and self.abs + x < r.width and self.ord + y > 0 and self.ord + y < r.height :
            self.abs += x
            self.ord += y
            return True
        else :
            return False

    def action(self, act, r):
        x = {'l': -1, 'r': 1, 'u': 0, 'd': 0}[act]
        y = {'d': -1, 'u': 1, 'l': 0, 'r': 0}[act]
        for c in r.characters :
            if c.abs == self.abs + x and c.ord == self.ord + y :
                self.hits(c)
                return True
        self.moves(act,r)
