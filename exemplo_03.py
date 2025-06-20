nome = "Manoela"
print(len(nome))

slice1 = nome[0:2]
print(slice1)

slice2 = nome[len(slice1):len(slice1)+2]
print(slice2)

slice3 = nome[-3:]
print(slice3)

nome = slice1+slice2+slice3
print(nome)
