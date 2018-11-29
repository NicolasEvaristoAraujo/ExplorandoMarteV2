import sys
import math
import pdb
from classe import Coordenadas

cord = Coordenadas()
direct = {'E': 360, 'W': 180, 'N': 90, 'S': 270}

angulo          = 0
limiteX         = 0
limiteY         = 0
X               = 0
Y               = 0

# Interpreta os comandos de movimento
def moveSonda( string ):
    for letra in string:
        if letra == 'L':
            cord.direcao += 90
            
        elif letra == 'R':
            cord.direcao -= 90
            
        elif letra == 'M':
            angulo = ((360 * 2) * math.pi)/360

            cord.posX += int(math.cos(angulo))
            if cord.posX > limiteX:
                cord.posX = limiteX
            elif cord.posX < 0:
                cord.posX = 0
                
            cord.posY += int(math.sin(angulo))
            if cord.posY > limiteY:
                cord.posY = limiteY
            elif cord.posY < 0:
                cord.posY = 0;

        cord.direcao %= 360
        if cord.direcao < 0:
            cord.direcao += 360

def printSondaPosition():
    dirName = ("E", "N", "W", "S")
    print("Posicao atual da sonda é")
    print("%d %d %s \n" %(cord.posX, cord.posY, dirName[ int(cord.direcao / 90) ]))

def main():
    print("***************************************")
    print("******* Explorando Marte - V2 *********")
    print("***************************************")

    print("\n\n Entre com os limites superiores do quadrante ( X, Y )")
    limiteX, limiteY = input("X Y: ").split(" ")

    limiteX = int( limiteX )
    limiteY = int( limiteY )
    
    print("Entre com as coordenadas e a direcao da sonda (X, Y, D)")
    print("As posiveis direcoes sao N, W, S ou E")
    X, Y, D = input("X Y D: ").split(" ")

    cord.direcao = direct[D]
    cord.posX = int(X)
    cord.posY = int(Y)

    print("Entre com os comandos para mover a sonda (L, R ou M)")
    string = input(" ")
    moveSonda(string)

    printSondaPosition()

if __name__ == '__main__':
    main()
