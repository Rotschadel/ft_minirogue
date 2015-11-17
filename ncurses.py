import curses
from Player import Player


class Room(object):
    def __init__(self, w, h, y, x, path, is_room=True):
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
        else:
            for p in room.path:
                self.win.addstr(p[0], p[1], "p")
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
rooms.append(Room(5, 7, 1, 1, []))
rooms.append(Room(8, 8, 10, 10, []))
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
