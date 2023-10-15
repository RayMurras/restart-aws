print("Colocação do piloto")
piloto = int(input())
pontos= 0
if( piloto == 1):
    pontos = 10
    print("Ganhou", pontos, "pontos")

if( piloto == 2):
    pontos = 8
    print("Ganhou", pontos, "pontos")

if( piloto == 3):
    pontos = 6
    print("Ganhou", pontos, "pontos")

if( piloto == 4):
    pontos = 5
    print("Ganhou", pontos, "pontos")

if( piloto == 5):
    pontos = 4
    print("Ganhou", pontos, "pontos")

if( piloto == 6):
    pontos =3
    print("Ganhou", pontos, "pontos")

if( piloto == 7):
    pontos = 2
    print("Ganhou", pontos, "pontos")

if( piloto == 8):
    pontos = 1
    print("Ganhou", pontos, "pontos")

if( piloto > 8):

    print("Não ganhou pontos")