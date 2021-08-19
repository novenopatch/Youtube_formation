import os
import math
print("\t Ce script affiche les puissance de 2")
n = int(input("Veille enter la puissance maximale>:"))
somme = 0
for k in range(1, n+1):
    somme += math.pow(2, k)

print("La somme de 2 puissance n =", n , "donne :",somme)


os.system("pause")