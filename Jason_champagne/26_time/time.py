#coding:utf-8
import time



# 1er janvier 1970 à 00h00

#time.sleep(5)#il créer une pause dans le programme

#print(time.time()) # affiche time (2038 pour le 32bit) #chez jason le temp affiché est : 1519739033.432446
"""
begin = time.time()
print("début")

time.sleep(5)

end = time.time()
print("Fin")

print("Temps exécuté : ", end - begin,"s")
"""


"""
print(time.localtime())

                localtime()
(TIMESTAMP)---------------------> Structure de temps
           <-------------------
                mktime()

            exemple de parcours:
            tps = time.localtime()
            print(tps)
            tps = time.mktime(tps)
            print(tps)


"""

"""
%d : jours (01 à 31)
%m : mois (01 à 12)
%Y : année (ex : 2018) - %y (00 à 99)
%H : heures (00 à 23)
%I : minute (00 à 59)
%S : secondes (00 à 59)
%p : AM/PM

%A : jour semaine / %a (jour abrégé)
%B: mois / %b (mois abrégé)

%Z : fuseau horaire (timezone)

 time.strftime()
Exemple: print(time.strftime("%a"))

bef:
time.sleelp(<int en seconde>)
    .time()
    .localtime()
    .mktime()
    .strftime()
"""
print(time.strftime("%Z"))




