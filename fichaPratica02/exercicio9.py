print("Digite um número")
num1 = int(input())

print("Digite outro número")
num2 = int(input())

print("Digite outro número")
num3 = int(input())

if(num1 != num2 != num3):

    if(num1<num2 and num1<num3):
        print("O menor número é:", num1)

    if(num2<num1 and num2<num3):
        print("O menor número é:", num2)

    if(num3<num1 and num3<num2):
        print("O menor número é:", num3)

else:
    print("São iguais")
