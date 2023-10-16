valor = int(input("Digite um valor em euros: "))

if(valor % 5 == 0):

    if (valor >= 200):
        nota200 = int(valor / 200)
        print("Notas de 200:", nota200)
        valor =200 * nota200 - valor

    if (valor >= 100):
        nota100 = int(valor / 100)
        print("Notas de :100", nota100)
        valor = valor - 100 * nota100

    if (valor >= 50):
        nota50 = int(valor / 50)
        print("Notas de 50:", nota50)
        valor = valor - 50 * nota50

    if (valor >= 20):
        nota20 = int(valor / 20)
        print("Notas de 20:", nota20)
        valor = valor - 20 * nota20

    if (valor >= 10):
        nota10 = int(valor / 10)
        print("Notas de 10:", nota10)
        valor = valor - 10 * nota10


    if (valor >= 5):
        nota5 =int(valor/ 5)
        print("Notas de 5:", nota5)
        valor = valor-5 * nota5

else:
    print("Não há troco.")









