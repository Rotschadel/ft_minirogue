import curses
from ncurses import *
from Personnage import *
from Player import *
from Enemy import *
from Level import *
from Item import *

class RogueLike(object) :
    """
    def dungeonTurn(r):
        for c in r.characters :

    """


    nom = input("nom : ")
    player = Player(nom)
    touche = 'o'
    while touche != 'q':
        for r in rooms :
            displayRoom(r)
        activeRoom = player.isInRoom()
        while True :
            if player.action(touche, activeRoom):
                break
        #dungeonTurn(activeRoom)
        if player.isDead() :
            touche = 'q'
        elif stdscr.getch() in [258,259,260,261,27,ord('q')] :
            touche = {259:'u', 258:'d',260:'l',261:'r',27:'q',ord('q'):'q'}[stdscr.getch()]
