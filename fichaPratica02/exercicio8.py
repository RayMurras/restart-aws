print("nota1")
nota1 = float(input())

print("nota2")
nota2 = float(input())

print("nota3")
nota3 = float(input())

mediaFim = ((nota1 * 0.25) + (nota2 * 0.35) + (nota3 * 0.4)) / 3
print("A media final será:", mediaFim)

if(mediaFim > 9.5):
    print("Aluno aprovado")

else:
    print("Aluno reprovado")