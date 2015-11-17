class Item(object) :
    def __init__(self, category, level, x, y):
        self.type = category
        self.lvl = Level(level)
        self.ammount = level * 8
        self.abs = x
        self.ord = y
