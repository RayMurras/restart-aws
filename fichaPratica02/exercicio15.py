print("Digite um número")
num1 = int(input())

print("Digite outro número")
num2 = int(input())

print("Digite outro número")
num3 = int(input())

if(num1 != num2 != num3):
    
    print("Deseja exibir em ordem crescente(c) ou decrecente(d)?")
    opcao=input()

    if(opcao=="c"):

        if(num1<num2 and num1<num3 and num2<num3):
            print(num1, num2, num3)

        if(num2>num1 and num2>num3 and num3>num1):
            print(num1, num3,num2 )

        if(num2<num1 and num2<num3 and num3<num1):
            print(num2, num3,num1 )

        if(num2<num1 and num2<num3 and num3>num1):
            print(num2, num1,num3 )

        if(num2>num1 and num2<num3 and num3<num1):
            print(num3, num1,num2 )

        if(num2<num1 and num2<num3 and num3<num1):
            print(num3, num2,num1 )

    if(opcao=="d"):

        if(num1>num2 and num1>num3 and num2>num3):
            print(num1, num2, num3)

        if(num2<num1 and num2<num3 and num3<num1):
            print(num1, num3,num2 )

        if(num2>num1 and num2>num3 and num3>num1):
            print(num2, num3,num1 )

        if(num2>num1 and num2>num3 and num3<num1):
            print(num2, num1,num3 )

        if(num2<num1 and num2>num3 and num3>num1):
            print(num3, num1,num2 )

        if(num2>num1 and num2>num3 and num3<num1):
            print(num3, num2,num1 )


else:
    print("São iguais")
