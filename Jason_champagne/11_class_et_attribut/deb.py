class Humain :
    """
    Docstring
    
    """
    humains_crées = 0 #attribut de class tout le monde peut y accédé

    def __init__(self, classprenom ="?" , classage =1):#class* sont des attributs
        #pass # cela veut dire il fait rien normalement  le pass est remplacé par des instruction
        #self.prenom = classprenom
        #self.age = classage
        Humain.humains_crées +=1
#object :variable d'une class
#h1 = Humain("jit",45)  #cette commande créé l'humain h1
#print("{}".format(h1.prenom))
#h2 = Humain("kart", 23)