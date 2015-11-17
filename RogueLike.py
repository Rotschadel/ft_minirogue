import curses
from ncurses import *
from Personnage import *
from Player import *
from Enemy import *
from Level import *
from Item import *
from Room import *
from random import *
class RogueLike(object) :

    def dungeonTurn(player, r):
        for c in r.characters :
            if not c.isPlayer :
                c.movesToPlayer(player, r)

    def searchItem(player, r):
        for i in r.items :
            if i.abs == player.abs and i.ord == player.ord :
                player.grabsItem(i)

    def fill(r,n):
        r.characters += Enemy(Enemy, n, r.width/2, r.height/2)
        k = randint(0,3)
        r.item += Item(["meat","treasure","weapon","armour"][k], n, r.width, r.height)

    nom = raw_input("nom : ")
    player = Player(nom)
    touche = 'o'
    while touche != 'q':
        for r in rooms :
            r.display()
        activeRoom = player.room
        activeRoom.characters += player
        k=0
        if activeRoom.is_room :
            for i in range(len(rooms)):
                if rooms[i] == activeRoom:
                    k=i
            fill(activeRoom, i)
        while True :
            if player.action(touche, activeRoom):
                break
        searchItem(player, activeRoom)
        dungeonTurn(player, activeRoom)
        if player.isDead() :
            touche = 'q'
        elif stdscr.getch() in [258,259,260,261,27,ord('q')] :
            touche = {259:'u', 258:'d',260:'l',261:'r',27:'q',ord('q'):'q'}[stdscr.getch()]
