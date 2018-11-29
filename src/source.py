import sys
from classe import sonda as sd

print("\n\n***************************************")
print("******* Explorando Marte - V2 *********")
print("***************************************\n\n")

print("Entre com os limites do quadrante ( X, Y ) \n")
limiteX, limiteY = input("( X, Y ): ").split(" ")
string = input("Entre com a palavra: ")

limiteX = int(limiteX)
limiteY = int(limiteY)

def setLimite( x, y ):
    limiteX = x
    limiteY = y

def setPosicao( x, y, direcao ):
    sd.set_posX(x)
    sd.set_posY(y)
    sd.set_dir(direcao)
    
def moveSonda( string  ):
    angulo = 0
    
    for letra in string:
        print(letra)


moveSonda(string)

