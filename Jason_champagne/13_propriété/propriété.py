#coding:utf-8
"""
Propriété : maniere de manipuler/controler des attributs
                            principe d'encapsulation!
                            exemple ici: age = property(_getage, _setage, _delage,)
                            le menento c'est ce fichers


"""
class Humain:
    """ CETTE CLASSE REPRESENTE UN HUMAIN.  cmd pour : help() ici help(Humain)    """

    def __init__(self, nom, age, ):
        self.nom = nom
        self._age = age




    def _getage(self):
        if self._age <= 1:
            return str(self._age) + " an ."#le meillur moyen cést de faire: "{} {}".format(self._age, "an")
        else:
            return str(self._age) + " ans ."#le meillur moyen cést de faire: "{} {}".format(self._age, "ans")


        """
        try:
            return self._age
        except AttributeError :
            print("L'age n'existe pas !")

    def _setage(self,new_age):
        if new_age <= 0:
            self._age = 0
        else :
            self._age = new_age
    def _delage(self ):
        del self._age
        """
        #property(<getter>,<setter>,<deleter>, helper)
    age = property(_getage) #, _setage , _delage , "age variable qui definie l'age d'une humain")


#h1 = Humain(1001, 5 )

#print(h1.age)

#h1.age = -12
#print(h1.age)
#help(Humain)

h1 = Humain("jason champagne", 1)


print("{} a {}".format(h1.nom, h1.age))




