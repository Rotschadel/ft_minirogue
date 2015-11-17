class Personnage (object):

    def __init__(self, nom, health, level, exp, attack, defense, wealth, x, y):
        self.name = nom
        self.hp = health
        self.lvl = level
        self.xp = exp
        self.strength = attack
        self.armour = defense
        self.gold = wealth
        self.abs = x
        self.ord = y

    def isHit(self, power):
        self.hp -= power

    def isDead(self):
        return self.hp < 0

    def hits(self, perso):
        if perso.lvl.defense + perso.armour - self.strength - self.lvl.attack < 0 :
            perso.hp -= self.strength + self.lvl.attack - perso.lvl.defense - perso.armour


    def moves(self, dir):
        x = {'l': -1, 'r': 1, 'u': 0, 'd': 0}[dir]
        y = {'d': -1, 'u': 1, 'l': 0, 'r': 0}[dir]
        self.abs, self.ord += x, y

    def action(self, act):
        if act=='s' :
            #hits
        elif act in ['u','d','l','r'] :
            self.moves(act)
