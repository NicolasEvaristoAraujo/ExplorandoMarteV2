# ExplorandoMarteV2

Explorando Marte - Versão 2

Um conjunto de sondas foi enviado pela NASA à Marte e irá pousar num planalto. Esse planalto, que curiosamente é retangular,
deve ser explorado pelas sondas para que suas câmeras embutidas consigam ter uma visão completa da área e enviar as imagens 
de volta para a Terra.

A posição e direção de uma sonda são representadas por uma combinação de coordenadas x-y e uma letra representando a direção
cardinal para qual a sonda aponta, seguindo a rosa dos ventos em inglês.

O planalto é dividido numa malha para simplificar a navegação. Um exemplo de posição seria (0, 0, N), que indica que a sonda 
está no canto inferior esquerdo e apontando para o Norte.

Para controlar as sondas, a NASA envia uma simples sequência de letras. As letras possíveis são "L", "R" e "M". 
Destas, "L" e "R" fazem a sonda virar 90 graus para a esquerda ou direita, respectivamente, sem mover a sonda. "M" faz com que 
a sonda mova-se para a frente um ponto da malha, mantendo a mesma direção.

Nesta malha o ponto ao norte de (x,y) é sempre (x, y+1).

ENTRADA:
A primeira linha da entrada de dados é a coordenada do ponto superior-direito da malha do planalto. A inferior esquerda sempre
será (0,0).
O resto da entrada é informação das sondas que foram implantadas. Cada sonda é representada por duas linhas. A primeira 
indica sua posição inicial e a segunda uma série de instruções indicando para a sonda como ela deverá explorar o planalto.
A posição é representada por dois inteiros e uma letra separados por espaços, correspondendo à coordenada X-Y e à direção da sonda. 
Cada sonda é controlada sequencialmente, a segunda sonda só irá se movimentar após que a primeira tenha terminado suas instruções. 

SAÍDA:
A saída conta uma linha para cada sonda, na mesma ordem de entrada, indicando sua coordenada final e direção.
