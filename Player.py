from Personnage import *
from Item import *
from Level import *
from Room import *

class Player (Personnage) :

    def __init__(self, nom):
        l = Level(1)
        Personnage.__init__(self, nom, l.maxHp, l, 0, 0, 0, 0, 1, 1, True )

    def collectsWeapon(self, ammount):
        self.strength = ammount

    def collectsArmour(self, ammount):
        self.armour = ammount

    def collectsTreasure(self, ammount):
        self.gold += ammount

    def collectsMeat(self, ammount):
        if self.hp + ammount <= self.lvl.maxHp :
            self.hp += ammount
        else :
            self.hp = self.lvl.maxHp

    def grabsItem(self, item):
        {"meat":self.collectsMeat(item.ammount), "treasure":self.colectsTreasure(item.ammount), "armour":self.colectsArmour(item.ammount), "weapon":self.colectsWeapon(item.ammount)}[item.type]

    def LevelUp(self):
        self.lvl = Level(self.lvl.numero+1)
        self.hp += 10

    def canLevelUp(self):
        return self.xp > self.lvl.xpToNext

    def isInRoom(self, t):
        for r in t :
            if self.abs > r.pos_x and self.abs < r.pos_x+r.width and self.ord > r.pos_y and self.ord < r.pos_y+r.height :
                return r

    def move(self, key):
        if key == None:
            return False
        x = self.abs
        y = self.ord
        if key == "down":
            y += 1
        elif key == "up":
            y -= 1
        elif key == "left":
            x -= 1
        elif key == "right":
            x += 1
        if x <= 0 or x >= self.room.height - 1:
            return False
        if y <= 0 or y >= self.room.width - 1:
            return False
        self.abs = x
        self.ord = y
        return True
