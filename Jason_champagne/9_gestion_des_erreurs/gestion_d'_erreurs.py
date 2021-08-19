#coding:utf-8

"""
on doit verifier les instructions : 

exemple1: (pour la methode la plus simpliciste bah la plus fénéante aussi)
age = input("rrrrrrrrrrrrrrrrr")
try:
    age = int(age)
    #les instructions
except:
    print("Vous avez saisie des informations incorrecte")

le problème avec l'exemple1 x k le programme s'arrete qu'a mème


exemple2:
age = input("rrrrrrrrrrrrrrrrr")
try:
    age = int(age)
    #les instructions
except:
    print("Vous avez saisie des informations incorrecte")
else:
    #les instructions


exemple3:
age = input("rrrrrrrrrrrrrrrrr")
try:
    age = int(age)
    #les instructions
except:
    print("Vous avez saisie des informations incorrecte")
else:
    #les instructions
finally:#quelque soit ce qui se passe l'instruction ou les à executé

exemple4:
try:
except <nom_de_l'erreur_que_python_affiche_>#il suffit de faire les test dans l'interpreteur:
    <instruction>
except <>:

except <>:

except <>:

else:

finally:

#a utiliser pour demain comment créer nos propre erreur
conditon:
    raise <nom_de_l'erreur>
except <nom_de_l'erreur>:
    <>

autres truc:
try :
    age =input("")"
    age = int(age)
assert age < 0 #je veux que l'age soit plus grand que 0
except AssertionError :
    print("l'age est inférieur à zero")


"""