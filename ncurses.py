import curses
import time


class Room(object):
    def __init__(self, h, w, x, y):
        self.height = h
        self.width = w
        self.pos_x = x
        self.pos_y = y

class GUI(object):

    def __init__(self):
        stdscr = curses.initscr()
        curses.curs_set(False)

    def __del__(self):
        curses.endwin()

    def display():
        stdscr.clear()
        stdscr.addstr(10, 10, "test")
        time.sleep(2)
        stdscr.refresh()

#g = GUI()
stdscr = curses.initscr()
curses.curs_set(False)
stdscr.addstr(10, 10, "test")
stdscr.keypad(1)
while True:
    c = stdscr.getch()
    if c == 27:
        break
    stdscr.clear()
    if c == 32:
        stdscr.addstr(10, 10, "space")
    elif c < 256:
        stdscr.addstr(10, 10, "test " + chr(c))
    else:
        stdscr.addstr(10, 10, str(c))
    stdscr.refresh()
curses.endwin()
