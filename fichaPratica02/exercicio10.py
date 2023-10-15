print("Escreva um número")
num1 = int(input())

print("Escreva outro número")
num2 = int(input())

print("escolha a operação: +, *, -, /")
operacao = (input())

if( operacao == "+"):

    soma = num1 + num2
    print("O resultado da soma:", soma)

if( operacao == "-"):
    sub = num1 - num2
    print("O resultado da subtração:", sub)

if (operacao == "*"):
    multi = num1 * num2
    print("O resultado da multiplicação:", multi)

if (operacao == "/"):
    div = num1 / num2
    print("O resultado da divisão:", div)

if(operacao != "+" and "*" and "-" and "/"):
    print("erro")
