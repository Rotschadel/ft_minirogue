class Player (Personnage) :

    def __init__(self, nom):
        l = Level(1)
        Personnage.__init__(self, nom, l.maxHp, l, 0, 0, 0, 0, 0, 0 )

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
