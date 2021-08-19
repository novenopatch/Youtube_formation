import os
import math
calcul =0
#b= [0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
b=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for valeur in b:
    calcul = calcul + valeur
print(calcul, len(b))



def doTest():
    nbr = input("Veillez entrer un nombre de test:")
    nbr = int(nbr)
    while nbr != 0 :
        div =2
        premier = True
        while premier and div < nbr - 1: #div <= math.sqrt(nbr):#apres le and on aurait pu faire div < nbr - 1 qui marche aussi
            if nbr % div ==0:
                premier = False
            div +=1
        if premier:
                print("\t" , nbr,"est un nombre premier")
                nbr= 0
        else :
            print("\t",nbr,"n'est pas un nombre premier")
            #nbr = input("\t Veillez entrer un nouveau nombre de test et \t zero(0) pour quiter le programme:")
        nbr = input("\t Veillez entrer un nouveau nombre de test ou \t zero(0) pour quiter le programme:")




running = True
while running:
    try:
            doTest()
            running= False
            break
    except:
        print("saisie incorrecte Veillez saisir un nombre Svp \n")
        doTest()
        pass

os.system("pause")
