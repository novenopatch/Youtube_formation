import math
choix = "z"
while choix != "Q" and choix != "q":
        print("Conversion entier vers binaire......1")
        print("Cnversion binaire en entier........2")
        print("Quiter.............................Q")
        choix =input("Votre choix.........................")
        if choix =="1":
            #conersion entier vers binaireelse
            nbr = int(input("entrer un entier="))
            binaire =""
            while nbr !=0:
                reste = str(nbr % 2)
                binaire = reste + binaire
                nbr = nbr // 2
            print("Conversion en binaire=",binaire)
        else : 
            if choix=="2":
                #conversion binaire vers entier
                binaire = input("enter un nombre binaire =")
                k = 0
                nbr = 0
                while len(binaire)> 0:
                    b= int(binaire[len(binaire)-1:])
                    nbr += b*math.pow(2, k)
                    k +=1
                    binaire = binaire[: len(binaire)-1]
                print("Conversion en entier =", nbr)
                    