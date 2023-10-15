salario = float(input("Salario anual: "))
imposto =0
if( salario <= 15000):
    imposto = salario * 0.20
    print("A taxa a pagar é: ", imposto, "€")

else:
    imposto = salario * 0.30
    print("A taxa a pagar é: ", imposto, "€")