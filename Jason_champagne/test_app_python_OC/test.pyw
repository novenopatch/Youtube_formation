
#open_classroom apprendre le laguage python memento
"""
test = True
while test:
    age = input("VEILLEZ ENTRER VOTRE AGE:>")
    place_m =7
    place_M=12
    popcorn = 5
    try:
        age = int(age)
        if age < 18:
            print("Votre place de cinema vous couteras:" + str(place_m))
            dmd_p = input("Voulez vous des POPCORN?:>")
            if dmd_p == "True" or "true":
                print("Votre place de cinema vous couteras:{}$".format(place_m+popcorn))
                input("")
                test = False
            else :
                print("Votre place de cinema vous couteras:" + str(place_m))
                test = False
        elif age >=18:
             print("Votre place de cinema vous couteras:" + str(place_M))
             dmd_p = input("Voulez vous des POPCORN?:>")
             if dmd_p == "True" or "true":
                 print("Votre place de cinema vous couteras:{}$".format(place_M))
                 input("")
                 test = False
             else:
                 print("Votre place de cinema vous couteras:" + str(place_m))
                 test = False
                 
    except:
        print("Vous avez entrez une valeur incorecte ou rien du tout")
        continue
"""

"""
chaine= ""

while chaine.lower() != "q":
    chaine = input("Tapez une chaine")

print("BONJOUR")
 
"""


"""
def afficher_flottant(flottant, nc=3):#fonction cool
    #"
    Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères représentant la troncature de ce nombre. 
	La partie flottante doit avoir une longueur maximum de 3 caractères.
	De plus, on va remplacer le point décimal par la virgule
    #"
    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    longueur_flotant = len(flottant)
    if nc> longueur_flotant:
    	nb = 3
    elif nc<= longueur_flotant:
    	nb = nc
    partie_entiere, partie_flottante = flottant.split(".")
    # La partie entière n'est pas à modifier
    # Seule la partie flottante doit être tronquée
    if nc == 0:
        return partie_entiere
    return ",".join([partie_entiere, partie_flottante[:nb]])


tor =afficher_flottant(9.00001,0)
print(tor)
"""

"""
#compréhensions de liste 
#Parcours simple
liste_origine = [0, 1, 2, 3, 4, 5]
[nb * nb for nb in liste_origine]#------>[0, 1, 4, 9, 16, 25]

#Filtrage avec un branchement conditionnel

liste_origine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[nb for nb in liste_origine if nb%2==0]#----->[2, 4, 6, 8, 10]

#Mélangeons un peu tout ça:
qtt_a_retirer = 7 # On retire chaque semaine 7 fruits de chaque sorte 
fruits_stockes = [15, 3, 18, 21] # Par exemple 15 pommes, 3 melons... 
[nb_fruits-qtt_a_retirer for nb_fruits in fruits_stockes if nb_fruits>qtt_a_retirer] [8, 11, 14] 

#APPLICATION CONCRETE:
inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
    ]
#Pour ceux qui n'ont pas eu la curiosité de regarder dans la documentation des listes, je signale à votre attention la méthode sort qui permet de trier une liste. 
#Vous pouvez également utiliser la fonction sorted qui prend en paramètre la liste à trier (ce n'est pas une méthode de liste, faites attention). 
#sorted renvoie la liste triée sans modifier la liste d'origine, ce qui peut être utile dans certaines circonstances, précisément celle-ci. 
#À vous de voir, vous pouvez y arriver par les deux méthodes.
#Bien entendu, essayez de faire cet exercice en utilisant les compréhensions de liste.
#Je vous donne juste un petit indice : vous ne pouvez trier la liste comme cela, il faut l'inverser (autrement dit, placer la quantité avant le nom du fruit) pour pouvoir ensuite la trier par quantité.
#CORECTION
# On change le sens de l'inventaire, la quantité avant le nom
inventaire_inverse = [(qtt, nom_fruit) for nom_fruit,qtt in
inventaire]
# On n'a plus qu'à trier dans l'ordre décroissant l'inventaire inversé
# On reconstitue l'inventaire trié
inventaire = [(nom_fruit, qtt) for qtt,nom_fruit
in sorted(inventaire_inverse, \
   reverse=True)]


#Cela marche et le traitement a été fait en deux lignes.
#Vous pouvez trier l'inventaire inversé avant la reconstitution, si vous trouvez cela plus compréhensible. 
#Il faut privilégier la lisibilité du code
CORRECTION2:
# On change le sens de l'inventaire, la quantité avant le nom 
inventaire_inverse = [(qtt, nom_fruit) for nom_fruit,qtt in inventaire] 
# On trie l'inventaire inversé dans l'ordre décroissant
inventaire_inverse.sort(reverse=True)
# Et on reconstitue l'inventaire
inventaire = [(nom_fruit, qtt) for qtt,nom_fruit in inventaire_inverse)]

RESUME:
#On peut découper une chaîne en fonction d'un séparateur en utilisant la méthode split de la chaîne. 
#On peut joindre une liste contenant des chaînes de caractères en utilisant la méthode de chaîne join. Cette méthode doit être appelée sur le séparateur.
#On peut créer des fonctions attendant un nombre inconnu de paramètres grâce à la syntaxe def fonction_inconnue(*parametres): (les paramètres passés se retrouvent dans le tuple parametres). 
#Les compréhensions de listes permettent de parcourir et filtrer une séquence en en renvoyant une nouvelle. 
#La syntaxe pour effectuer un filtrage est la suivante : nouvelle_squence = [element for element in ancienne_squence if condition].


"""
"""
DICTIONAIRE: {}
mon_diction= {"bat":sit}
del mon_diction["bat"]#suprime bat et ça clé
mon_diction.pop("bat")#suprime aussi mais revoie la valeur de la clé suprimé
"""
"""
class Baton:
    def __init__(self,nom,age, valeur):
        self.nom = nom
        self.age = age
        self.valeur = valeur
        
    def parle(self):
        print("nom:{} ,age={},valeur={}".format(self.nom,self.age,self.valeur))

b1 = Baton("tom",12, 100)
b1.parle()
class Surface:
    
    object_nb= 0
    def __init__(self):
        self.surface =""
        
    def lire(self):
        print(self.surface)
    def ecrire(self,message):
        if self.surface != "":
            self.surface += "\n" + message
        else:
            self.surface = message
    def effacer(self):
        self.surface = ""
    def cero():#c'est une méthode de class sont premier paramètre n'est pas l'objet lui mm(self) mais la class elle meme
        print(object_nb)
    cero =staticmethod(cero)
s1 = Surface()
s1.ecrire("salut 1")
s1.lire()
s1.ecrire("salut 2")
s1.lire()
"""
top  ="zemo"
nova=top.find("e")
print(nova)
top1 =top.replace("e","*")
print(top1)