
min1 = int(input("munutos da musica 1:  "))
seg1 = int(input("segundos da musica 1:  "))

min2 = int(input("munutos da musica 2:  "))
seg2 = int(input("segundos da musica 2: "))

min3 = int(input("munutos da musica 3:  "))
seg3 = int(input("segundos da musica 3:  "))

min4 = int(input("munutos da musica 4:  "))
seg4 = int(input("segundos da musica 4:  "))

min5 = int(input("munutos da musica 5:  "))
seg5 = int(input("segundos da musica 5:  "))

minTotal = int((min1 + min2 + min3 + min4 + min5))
minToSeg = int((min1 + min2 + min3 + min4 + min5) * 60)
segTotal = int((seg1 + seg2 + seg3 + seg4 + seg5 + minToSeg))

hora = int(segTotal / 3600)
min = int((segTotal / 60)-(hora*60))
seg = int((segTotal)-(hora*3600)-(min*60))

print(hora, "h", min, "m", seg, "s")