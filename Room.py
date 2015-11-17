import curses

class Room(object):
    nb_rooms = 0
    rooms = []
    def __init__(self, w, h, y, x, path, is_room=True):
        self.id = "room-" + str(Room.nb_rooms)
        Room.nb_rooms += 1
        self.height = h
        self.width = w
        self.pos_x = x
        self.pos_y = y
        self.path = path
        self.win = curses.newwin(w, h, y, x)
        self.is_room = is_room
        self.item = []
        self.characters = []
    def display(self):
        self.win.clear()
        if self.is_room:
            self.win.box()
            self.win.bkgd('.')
        for p in self.path:
            self.win.addstr(p[0], p[1], '+')
        for c in self.characters:
            self.win.addstr(c.ord, c.abs, c.name[0])
        self.win.refresh()

class GUI(object):
    def __init__(self, player):
        self.player = player
        self.win = curses.newwin(5, 100, 40, 0)
        self.win.keypad(1)
    def display(self, debug=None):
        hits = "Hits:" + str(self.player.hp)
        hits += "(" + str(self.player.lvl.maxHp) + ")"
        strength = "Str:" + str(self.player.strength)
        strength += "(" + str(self.player.strength) + ")"

        self.win.clear()
        self.win.box()
        self.win.addstr(2, 2, "Level:" + str(self.player.lvl.num))
        self.win.addstr(2, 27, hits)
        self.win.addstr(2, 42, strength)
        self.win.addstr(2, 62, "Gold:" + str(self.player.gold))
        self.win.addstr(2, 82, "Armor:" + str(self.player.armour))
        if debug is not None:
            self.win.addstr(3, 3, debug)
        self.win.refresh()
