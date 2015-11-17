import curses
from Player import *
from Room import *

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
start = Room(5, 7, 1, 1, path)
start.characters.append(p)
rooms.append(start)
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

while True:
    c = g.win.getch()
    if c == 27 or c == ord('q'):
        break
    for r in rooms:
        r.display()
    g.display()
clear_curses()
