num= int(input("Escreva um número: "))

ant= num - 5
seg= num + 5
while(ant< num ):
    print(ant )
    ant += 1
num+=1

while(seg >= num ):
    print(num)
    num += 1