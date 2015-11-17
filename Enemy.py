from Personnage import *
from Level import *
class Enemy(Personnage) :
    def __init__(self, level, x, y, nom="Enemy",):
        l = Level(level)
        Personnage.__init__(self, nom, l.maxHp, l, level*30, 0, 0, level*7, x, y)

    def movesToPlayer(self, player, r):
        flag = False
        if player.abs > self.abs :
            flag = self.action('r', r)
        if not flag :
            if player.abs < self.abs :
                flag = self.action('l', r)
        if not flag :
            if player.ord > self.ord :
                flag = self.action('u', r)
        if not flag :
            if player.ord < self.ord :
                flag = self.action('d', r)
