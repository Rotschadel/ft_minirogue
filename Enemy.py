class Enemy(Personnage) :
    def __init__(self, nom, level, x, y):
        l = Level(level)
        Personnage.__init__(self, nom, l.maxHp, l, level*30, 0, 0, level*7, x, y)

    
