import sys
import math
from classe import Coordenadas

cord = Coordenadas()

direct = {'E': 360, 'W': 180, 'N': 90, 'S': 270}

angulo                  = 0;
x                       = 0;
y                       = 0;

def moveSonda( string ):
    for letra in string:
        if letra.upper() == 'L':
            cord.direcao += 90
            
        elif letra.upper() == 'R':
            cord.direcao -= 90
            
        elif letra.upper() == 'M':
            angulo = cord.direcao
            angulo = (angulo * 2 * math.pi)/360

            cord.pos[0] += int(math.cos(angulo))
            if cord.pos[0] > cord.limiteX:
                cord.pos[0] = cord.limiteX
            elif cord.pos[0] < 0:
                cord.pos[0] = 0
                
            cord.pos[1] += int(math.sin(angulo))
            if cord.pos[1] > cord.limiteY:
                cord.pos[1] = cord.limiteY
            if cord.pos[1] < 0:
                cord.pos[1] = 0

        cord.direcao %= 360
        if cord.direcao < 0:
            cord.direcao += 360

def printSondaPosicao():
    dirName = ("E", "N", "W", "S")
    print(" ")
    for i in range(0, nSondas):
        print("%d %d %s" %(cord.posicao_finalX.pop(0), cord.posicao_finalY.pop(0), dirName[ int((cord.direcao_final.pop(0)) / 90) ]))

    input("\nPressione ENTER para sair")
    return
    
def sondas():
    global nSondas
    nSondas = 2
    
    for n in range(0, nSondas):
        #Coordenadas e direcao da sonda (X, Y, D)
        x, y, d = input("X[%d] Y[%d] D[%d]:  " %((n+1),(n+1),(n+1))).split(" ")
        
        cord.direcao = direct[d]
        cord.pos = [int(x),int(y)]

        if ((cord.pos[0] > cord.limiteX) or (cord.pos[1] > cord.limiteY)):
            print("Entrada inválida, valor maior que o limite permitido")
            return
        
        #Entrada de dados para mover a sonda (L, R ou M)
        string = input("Entre com as direções S%d: " %(n+1))
        
        moveSonda(string)
        
        cord.posicao_finalX.insert(n, cord.pos[0])
        cord.posicao_finalY.insert(n, cord.pos[1])
        cord.direcao_final.insert(n, cord.direcao)
        
    printSondaPosicao()


def main():
    print(" \n\n ")
    print("***************************************")
    print("******* Explorando Marte - V2 *********")
    print("***************************************")
    print(" \n\n ")
    
    #Entrada de dados dos limites superiores do quadrante
    limiteX, limiteY = input("Ponto superior-direito: ").split(" ")

    cord.limiteX = int( limiteX )
    cord.limiteY = int( limiteY )
    
    sondas()
    
if __name__ == '__main__':
    main()
