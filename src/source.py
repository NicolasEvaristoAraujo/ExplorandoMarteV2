import sys
import math
from classe import Coordenadas

cord = Coordenadas()
direct = {'E': 270, 'W': 180, 'N': 0, 'S': 90}

#limiteX = int(limiteX)
#limiteY = int(limiteY)
#X       = int(X)
#Y       = int(Y)

def moveSonda( string ):
    angulo = 0

    for letra in string:
        if letra == 'L':
            cord.direcao += 90
        elif letra == 'R':
            cord.direcao -= 90
        elif letra == 'M':
            angulo = ((360 * 2) * math.pi)/360
            
            cord.posX += math.cos(angulo)
            if cord.posX > limiteX:
                cord.posX = limiteX
            elif cord.posX < 0:
                cord.posX = 0
                
            cord.posY += math.sin(angulo)
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
    
    print("Entre com as coordenadas e a direcao da sonda (X, Y, D)")
    print("As posiveis direcoes sao N, W, S ou E")
    X, Y, D = input("X Y D: ").split(" ")
    cord.direcao = direct[D]

    print("Entre com os comandos para mover a sonda (L, R ou M)")
    string = input(" ")
    moveSonda(string)

    printSondaPosition()

if __name__ == '__main__':
    main()
