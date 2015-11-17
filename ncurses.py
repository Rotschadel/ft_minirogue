import curses
from Player import *
from Room import *
from random import *
from Enemy import *
def init_curses():
    stdscr = curses.initscr()
    curses.curs_set(False)

def clear_curses():
    curses.endwin()

def dungeonTurn(player, r):
    for c in r.characters :
        if not c.isPlayer :
            c.movesToPlayer(player, r)

def searchItem(player, r):
    for i in r.items :
        if i.abs == player.abs and i.ord == player.ord :
            player.grabsItem(i)

def fill(r,n):
    r.characters.append(Enemy(n, r.width/2, r.height/2))
    k = randint(0,3)
    r.item.append(Item(["meat","treasure","weapon","armour"][k], n, r.width, r.height))

#name = raw_input("Enter your name: ")
p = Player("toto")

init_curses()
g = GUI(p)
path = [
    (2, 6, {id: "room-1", dir: "right"}),
]
start = Room(5, 7, 1, 1, path)
start.characters.append(p)
p.room = start
Room.rooms.append(start)
path = [
    (0, 3, {id: "room-1", dir: "up"}),
]
Room.rooms.append(Room(8, 8, 10, 10, path))
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
Room.rooms.append(Room(7, 6, 3, 8, path, False))
def get_key_map(key):
    if key == curses.KEY_DOWN:
        return "down"
    elif key == curses.KEY_UP:
        return "up"
    elif key == curses.KEY_LEFT:
        return "left"
    elif curses.KEY_RIGHT:
        return "right"
    return None
fill(start, 1)
while True:
    c = g.win.getch()
    if c == 27 or c == ord('q'):
        break
    p.move(get_key_map(c))
    for r in Room.rooms:
        r.display()
    #while True :
        #if p.action(chr(c), activeRoom):
        #    break
    #searchItem(p, activeRoom)
    #dungeonTurn(p, activeRoom)
    #if p.isDead() :
    #    touche = 'q'
    g.display(get_key_map(c))
clear_curses()
