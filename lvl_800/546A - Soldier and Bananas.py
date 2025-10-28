#A soldier wants to buy w bananas in the shop. 
# He has to pay k dollars for the first banana, 2k dollars for the second one and so on (in other words, he has to pay i·k dollars for the i-th banana).

#He has n dollars. How many dollars does he have to borrow from his friend soldier to buy w bananas?

#Input
#The first line contains three positive integers k, n, w (1  ≤  k, w  ≤  1000, 0 ≤ n ≤ 109), 
# the cost of the first banana, initial number of dollars the soldier has and number of bananas he wants.

#Output
#Output one integer — the amount of dollars that the soldier must borrow from his friend. If he doesn't have to borrow money, output 0.

#Examples
#InputCopy
#3 17 4
#OutputCopy
#13

input_inicial = input("")
split_do_input = input_inicial.split(" ")

custo_primeira_banana = int(split_do_input[0])
dolares_soldado = int(split_do_input[1])
bananas_requeridas = int(split_do_input[2])
custo_total = 0

for _ in range(bananas_requeridas+1):
    custo_total += _ * custo_primeira_banana

pedir_emprestado = custo_total - dolares_soldado

if pedir_emprestado < 0:
    print(0)
else:
    print(pedir_emprestado)