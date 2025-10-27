import math
coordenada_casa_elefante = int(input(""))

if coordenada_casa_elefante == 5:
    passos = 1
else:
    passos = math.ceil(coordenada_casa_elefante/5)

print(passos)
