hora = int(input("Digite a hora: "))

if(hora >= 0 and hora <= 24):

    min = int(input("Digite os minutos: "))


    if(hora > 12 ):
            horaA = hora - 12  

            if ( min > 60):
                horaB = int((min / 60) + horaA)
                minA = min % 60

                print(horaB, ":", minA, "PM")

            if(min <= 60 and min >= 0):
                horaB = hora -12
                print(horaA, ":", min, "PM")


    if(hora < 12 ):
            
        if ( min > 60):
            horaB = int((min / 60) + horaA)
            minA = min % 60

            print(horaB, ":", minA, "AM")

        
        if(min < 60 and min >= 0):
            horaB = hora - 12
            print(horaB, ":", min, "AM") 

else:    
    print("Horario invalido")


