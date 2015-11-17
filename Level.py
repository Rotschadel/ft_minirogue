class Level (object) :

    def __init__(self, numero):
        self.num = numero
        self.maxHp = 100 + 10 * (numero-1)
        self.attack = 30 + 3 * (numero-1)
        self.defense = 20 + 2 * (numero-1)
        self.xpToNext = 50 + 70 * (numero-1)
