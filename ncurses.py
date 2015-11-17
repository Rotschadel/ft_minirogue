import curses
import time


class Room(object):
    def __init__(self, w, h, y, x, path, is_room=True):
        self.height = h
        self.width = w
        self.pos_x = x
        self.pos_y = y
        self.path = path
        self.win = curses.newwin(h, w, x, y)
        self.is_room = is_room

def displayRoom(room):
    room.win.clear()
    if room.is_room:
        room.win.box()
    else:
        for p in room.path:
            stdscr.addstr(p[0], p[1], "p")
    room.win.refresh()

stdscr = curses.initscr()
curses.curs_set(False)
stdscr.keypad(1)

rooms = []
cors = []

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
    c = stdscr.getch()
    if c == 27 or c == ord('q'):
        break
    for r in rooms:
        displayRoom(r)
curses.endwin()
