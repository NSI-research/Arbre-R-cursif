from turtle import *


tracer(0, 0)
goto(0, -500)

def Arbre(N, Pos=[0, 0], Dist=500, Angle=90):
    
    if N == 0:        # Cas terminal
        forward(Dist)
        
    else:            # Cas récurcif
        forward(Dist)
        left(45)
        Pos = pos()
        Arbre(N-1, pos(), Dist//2, Angle+45)    # Appel récursif
        
        setheading(Angle)    # On reprend l'angle du noeud précedent
        
        up()             #
        goto(Pos)        # On retourne sur le noeud précédent
        down()           #
        
        right(45)
        Arbre(N-1, pos(), Dist//2, Angle-45)    # Appel récursif
        setheading(Angle)
        
left(90)
speed("fastest")
Arbre(0, [0, 0])
update()
