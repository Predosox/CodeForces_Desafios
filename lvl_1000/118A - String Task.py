#A. String Task

#Petya started to attend programming lessons. On the first lesson his task was to write a simple program. 
#The program was supposed to do the following: in the given string, consisting if uppercase and lowercase Latin letters, it:

#deletes all the vowels,
#inserts a character "." before each consonant,
#replaces all uppercase consonants with corresponding lowercase ones.
#Vowels are letters "A", "O", "Y", "E", "U", "I", and the rest are consonants. 
#The program's input is exactly one string, it should return the output as a single string, resulting after the program's processing the initial string.

#Help Petya cope with this easy task.

#Input
#The first line represents input string of Petya's program. This string only consists of uppercase and lowercase Latin letters and its length is from 1 to 100, inclusive.

#Output
#Print the resulting string. It is guaranteed that this string is not empty.

#Examples
#InputCopy
#tour
#OutputCopy
#.t.r
#InputCopy
#Codeforces
#OutputCopy
#.c.d.f.r.c.s
#InputCopy
#aBAcAba
#OutputCopy
#.b.c.b

palavra = input("")
vogais = ["a","e","i","o","u","y","A","E","I","O","U","Y"]
resposta = []


for letra in palavra:
    if letra not in vogais:
        resposta.append(f".{letra}")
        

print("".join(resposta).lower())

#Start: 14:46 // End: 15:02