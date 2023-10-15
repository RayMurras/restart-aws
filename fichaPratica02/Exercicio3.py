print("Salario anual")
salario = float(input())
imposto =0
if( salario <= 15000):
    imposto = salario * 0.20
    print("A taxa a pagar é", imposto)

if( salario > 15000 and salario <= 20000 ):
    imposto = salario * 0.30
    print("A taxa a pagar é", imposto)

if( salario < 20000 and salario <= 25000):
    imposto = salario * 0.35
    print("A taxa a pagar é", imposto)

else:
    imposto = salario * 0.40
    print("A taxa a pagar é", imposto)