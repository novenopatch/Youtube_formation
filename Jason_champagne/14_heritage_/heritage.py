#coding:utf-8

class Vehicule :

    def __init__(self , nom , Q_essence , ):
        self.nom = nom
        self.Q_essence = Q_essence
    def deplacer(self):
        print("Le Vehicule {} se deplace...".format(self.nom))



class Voiture(Vehicule):
   def __init__(self , nom_voiture , essence , puissance):
       Vehicule.__init__(self ,nom_voiture , essence)#lige in portante pour que cela fonctionne
       self.puissance = puissance

#v1 = Vehicule("F22 Raptor", 34000 )
v2 = Voiture("Toyota supra", 90 , 600)
#v2.deplacer()
#print(v2.nom , v2.puissance, "chevaux...")

#issubclass(<classe fille>,<classe mère>)
# isinstance (<objet> , <classe>)


print(isinstance())