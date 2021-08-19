#import datetime


"""
"""

"""
            .datetime(anné,mois,jour,heure,minute,seconde):

                d1 = datetime.datetime(2020, 3, 16, 10, 10,54)
                d2 = datetime.datetime(2018, 2, 28, 9, 36,42)
                on peut comparer d1 et d2


            .date(anné,mois,jour):

            d1 = datetime.datetime(2020, 3, 16, 10, 10,54)
            d2 = datetime.datetime(2018, 2, 28, 9, 36,42)
            print(d1.year)
            print(type(d1))
            


            t1 =datetime.time(23,00,49)

        form datetime import date
        now = date.today
        print(now)
        
        
        

        from datetime import datetime

        print(datetime.now())


        #print(datetime.datetime.now()) #il affiche la date actuelle correcte
        #print(datetime.date.today())  #lu il recupére juste la date de naissance

        Exemple de code pas trop sur(d'après le formateur):
        
        import datetime
        from datetime import date

        now = date.today()
        born = datetime.date(1999, 11, 24)
        print(f"{now.year - born.year} and.") #===> au terminal ça affiche: 21 days, 0:00:00 and.
        
        Exercice:
        créer un programme qui demande à l'utilisateur d'entre sa date de naissance puis grace au module time,une fonction utilisant time et la date de today calculeras l'age de la personne.
        
"""
import datetime
from datetime import date
now = date.today()
born = datetime.date(1999, 11, 24)
print(f"{now.year - born.year} and.")


#input("Presser entrée pour quitter")