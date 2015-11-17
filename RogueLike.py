class RogueLike(object) :
    nom = input("nom : ")
    player = Player(nom)
    touche = 'o'
    while touche != 'q':
        player.action(touche)
        #gestion lieu (nouvelle salle, couloir, porte, pas autorise)
        if player.isDead() :
            touche = 'q'
        else :
            touche =
