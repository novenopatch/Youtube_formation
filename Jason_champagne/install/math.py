#coding:utf-8
import math

number = 14.6
entiersup = math.ceil(number)#affiche la valeur entier sup
entierinf = math.floor(number)#affiche la valeur  arrondi

racine_carre= math.sqrt(number)

puissance_m = math.pow(number,3)#puissance 3
valeur_absolue = math.fabs(number)#valeur absolue

number = 14
factoriel_d_un_nombre =  math.factorial(number) # biensur un entier

valeur_exponentielle = math.exp(number)#exponetielle
valeur_logarithme = math.log(number,2) #base 2 ou base 10,la générique
valeur_logarithme_bas2 = math.log2(number)#il sont plus précis que la version générique
valeur_logarithme_bas10 = math.log10(number)#plus précis
sinus_number = math.sin(number)

cosinus_number = math.cos(number)

tangente_number = math.tan(number)#pour les arc il suffit de mettre: acos,atan,asin

nb_degre = 110
nbr_degre_en_radian = math.radians(nb_degre)

nb_r = math.degrees(nbr_degre_en_radian)

mava = 23
mavar = math.isnan(mava)

print("Not a number {}".format(mavar))#false = is nombre, true = n'est pas un nombre

#module c math pour math complexe python

pi = math.pi
e = math.e
val = input("Tapez Entrer pour quiter............................. ")
