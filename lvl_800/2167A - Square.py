#A. Square?

#You are given 4
# sticks of lengths a
#, b
#, c
#, and d
#. You can not break or bend them.

#Determine whether it is possible to form a square∗
 #using the given sticks.

#∗
#A square is defined as a polygon consisting of 4
# vertices, of which all sides have equal length and all inner angles are equal. No two edges of the polygon may intersect each other.

#Input
#The first line contains a single integer t
 #(1≤t≤104
#) — the number of test cases.

#The only line of each test case contains four integers a
#, b
#, c
#, and d
# (1≤a,b,c,d≤10
#) — the lengths of the sticks.

#Output
#For each test case, print "YES" if it is possible to form a square using the given sticks, and "NO" otherwise.

#You may print each letter in any case (uppercase or lowercase). For example, the strings "yEs", "yes", "Yes", and "YES" will all be recognized as a positive answer.

#Example
#InputCopy
#7
#1 2 3 4
#1 1 1 1
#2 2 2 2
#1 2 1 2
#1 1 5 5
#5 5 5 5
#4 10 5 9
#OutputCopy
#NO
#YES
#YES
#NO
#NO
#YES
#NO
#Note
#In the first test case, we can prove that we can't make a square.

casos = int(input(""))
respostas = []

for _ in range(casos):
    comprimentos = list(map(int, input().split()))
    
    if len(set(comprimentos)) == 1:
        respostas.append("YES")
    else:
        respostas.append("NO")


print("\n".join(respostas))

#Ideia simples, remove duplicatas com o set(), logo, se só sobrar 1 então tudo é igual!
#Start: 09:00 // End: 09:12