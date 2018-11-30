import sys
import math
from classe import Coordenadas

cord = Coordenadas()
direct = {'E': 360, 'W': 180, 'N': 90, 'S': 270}

angulo              = 0
X                   = 0
Y                   = 0

def moveSonda( string ):
    for letra in string:
        if letra == 'L':
            cord.direcao += 90
            
        elif letra == 'R':
            cord.direcao -= 90
            
        elif letra == 'M':
            angulo = cord.direcao
            angulo = (angulo * 2 * math.pi)/360

            cord.posX += int(math.cos(angulo))
            if cord.posX > cord.limiteX:
                cord.posX = cord.limiteX
            elif cord.posX < 0:
                cord.posX = 0
                
            cord.posY += int(math.sin(angulo))
            if cord.posY > cord.limiteY:
                cord.posY = cord.limiteY
            if cord.posY < 0:
                cord.posY = 0

        cord.direcao %= 360
        if cord.direcao < 0:
            cord.direcao += 360

def printSondaPosition():
    dirName = ("E", "N", "W", "S")
    print("%d %d %s \n" %(cord.posX, cord.posY, dirName[ int(cord.direcao / 90) ]))

def sondas():
    #Coordenadas e direcao da sonda (X, Y, D)
    X, Y, D = input("X Y D: ").split(" ")
        
    cord.direcao = direct[D]
    cord.posX = int(X)
    cord.posY = int(Y)
        
    #Entrada de dados para mover a sonda (L, R ou M)
    string = input("L R ou M: ")
        
    moveSonda(string)

def main():    
    print("***************************************")
    print("******* Explorando Marte - V2 *********")
    print("***************************************")

    #Entrada de dados dos limites superiores do quadrante
    limiteX, limiteY = input("X Y: ").split(" ")

    cord.limiteX = int( limiteX )
    cord.limiteY = int( limiteY )

    sondas()
    printSondaPosition()

if __name__ == '__main__':
    main()
