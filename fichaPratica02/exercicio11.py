saldo = float(input("Digite o saldo: "))
montante = float(input("Digite o montante à debitar/creditar: "))

print(("Deseja debitar ou creditar?"))
operacao = input()

if( operacao == "debitar"):
    contaD = saldo - montante

    if(saldo >= montante):
        
        print("Operação realizada\n", saldo, "-", montante, "=", contaD)
    else:
        print("Saldo insuficiente\n", saldo, "-", montante, "=", contaD)


    
if(operacao == "creditar"):
    if(montante > 0):
    
        contaC = saldo + montante
        print("Operação realizada!\n", saldo, "+", montante, "=", contaC)
    

    if(montante == 0):
        print("Nenhum valor a creditar: \nSaldo:", saldo )

    else:
       print("Não é possivel realizar a operação\n", saldo) 


    