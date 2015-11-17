import curses
from Player import Player


class Room(object):
    nb_rooms = 0
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
    def display(self):
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
        self.win.refresh()

def init_curses():
    stdscr = curses.initscr()
    curses.curs_set(False)

def clear_curses():
    curses.endwin()


init_curses()
rooms = []
cors = []
p = Player("toto")
g = GUI(p)
path = [
    (2, 6, {id: "room-1", dir: "right"}),
]
rooms.append(Room(5, 7, 1, 1, path))
path = [
    (0, 3, {id: "room-1", dir: "up"}),
]
rooms.append(Room(8, 8, 10, 10, path))
path = [
    (0, 0, {id: "room-0", dir: "left"}),
    (0, 1, None),
    (0, 2, None),
    (0, 3, None),
    (0, 4, None),
    (0, 5, None),
    (1, 5, None),
    (2, 5, None),
    (3, 5, None),
    (4, 5, None),
    (5, 5, {id: "room-2", dir: "down"}),
    #(6, 5, "room-2"),
]
rooms.append(Room(7, 6, 3, 8, path, False))
"""
path = [
    (20, 20),
    (20, 21),
    (20, 22),
    (21, 22),
    (22, 22),
]
rooms.append(Room(5, 5, 15, 15, path, False))
"""

while True:
    c = g.win.getch()
    if c == 27 or c == ord('q'):
        break
    for r in rooms:
        r.display()
    g.display()
clear_curses()
