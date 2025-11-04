

# Usei map(int, input().split()) para:
# dividir a string em partes (split)
# converter cada parte para inteiro (map)
# transformar o resultado em uma lista (list)

linha1 = list(map(int, input().split()))
linha2 = list(map(int, input().split()))
linha3 = list(map(int, input().split()))
linha4 = list(map(int, input().split()))
linha5 = list(map(int, input().split()))

x_inicial = 0
y_inicial = 0

matriz = [linha1, linha2, linha3, linha4, linha5]

# Encontra a posição do número 1
for y, linha in enumerate(matriz):
    for x, numero in enumerate(linha):
        if numero == 1:
            x_inicial = x
            y_inicial = y

x_centro = 2
y_centro = 2

passos = 0

# Calcula os passos mínimos até o centro
while x_inicial != x_centro or y_inicial != y_centro:
    if x_inicial < x_centro:
        x_inicial += 1
    elif x_inicial > x_centro:
        x_inicial -= 1   
    elif y_inicial < y_centro:
        y_inicial += 1
    elif y_inicial > y_centro:
        y_inicial -= 1

    passos += 1

print(passos)