from Personnage import *
from Level import *
class Enemy(Personnage) :
    def __init__(self, nom="Enemy", level, x, y):
        l = Level(level)
        Personnage.__init__(self, nom, l.maxHp, l, level*30, 0, 0, level*7, x, y)
    """
    def movesToPlayer(self, player, r):
        flag = False
        if player.abs > self.abs :
            flag = self.moves('r', r)
        if ! flag :
    """    
