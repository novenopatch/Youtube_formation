class Humainm:
    lieu_habitation = "Terre"

    univer_d = "univer1"
#les méthode de class influe sur la classe en générale et nom un objet de la classe
    def __init__(self,nom,age):
        self.nom = nom
        self.age = age


    def parler(self, message):
        print("{} a dit : {}".format(self.nom, message))


    def changer_p(cls, new_p):#cls = méthode de classe
        Humainm.lieu_habitation = new_p
    changer_p = classmethod(changer_p)


    def changer_un(cls, new_un):
        Humainm.univer_d = new_un
    changer_un = classmethod(changer_un) 

    def définition():
        print("L'humain est mort.")
    définition = staticmethod(définition)
 #on doit créer une instance ici hm1 pou pour pouvoir utiliser  parler
#programme principale
hm1 = Humainm("tim", 20)


hm1.parler("Bonjour à tous ! :)")#c'est l'appel qui est un peu différent

print("Planète actuelle :{}".format(Humainm.lieu_habitation))

Humainm.changer_p("Jupiter")

print("Planète actuelle :{}".format(Humainm.lieu_habitation))


#pour mon affaire d'univer  actuelle et nouveau
print("Univers actuelle : {}".format(Humainm.univer_d))

#la fonction suivante permet fait appelle à la methode changer_un qui prend comme paramètre new_un qui change la valeur de la mèthode de classe univer_d
Humainm.changer_un("Gokou univers")

print("Univers actuelle : {}".format(Humainm.univer_d))

Humainm.définition()