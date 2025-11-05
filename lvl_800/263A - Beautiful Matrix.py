#A. Beautiful Matrix


#You've got a 5 × 5 matrix, consisting of 24 zeroes and a single number one. 
# Let's index the matrix rows by numbers from 1 to 5 from top to bottom, let's index the matrix columns by numbers from 1 to 5 from left to right. 
# In one move, you are allowed to apply one of the two following transformations to the matrix:

#Swap two neighboring matrix rows, that is, rows with indexes i and i + 1 for some integer i (1 ≤ i < 5).
#Swap two neighboring matrix columns, that is, columns with indexes j and j + 1 for some integer j (1 ≤ j < 5).
#You think that a matrix looks beautiful, if the single number one of the matrix is located in its middle 
# (in the cell that is on the intersection of the third row and the third column). Count the minimum number of moves needed to make the matrix beautiful.

#Input
#The input consists of five lines, each line contains five integers:
#the j-th integer in the i-th line of the input represents the element of the matrix that is located on the intersection of the i-th row and the j-th column. 
# It is guaranteed that the matrix consists of 24 zeroes and a single number one.

#Output
#Print a single integer — the minimum number of moves needed to make the matrix beautiful.



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