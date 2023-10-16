print("Salario médio anual:")
salario = float(input())
credito =0
if( salario <= 2000 and salario <= 0):
    print("Nenhum credito")

if(salario > 2000 and salario <= 4000):
    credito = salario * 0.20
    print("Credito disponivel:", credito)

if( salario < 4000 and salario <= 6000):
    credito = salario * 0.30
    print("Credito disponivel:", credito)

if(salario > 6000.00):
    credito = salario * 0.40
    print("Credito disponivel:", credito)