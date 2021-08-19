"""
              <> = {<> : <valeur>}
              dico = {} : vide

              dico = {1:000000000 , "clé":"val5"}

              print(dico["clé"])
              
              ajout : 
              dico["chien"] = " Animal con "

              del :
              dico.pop("chien") #on peut mettre mettre la sortie de pop dans une variable

              del dico["chien"] 

              if "chien" in dico:
                  print("oui")
              else :
                  print("Non")  

               
               
               for key in dico.keys():
                   print(key)

            
                for key in dico.values():

                for k, v in dico.items():
                    print("clé : {} - valeur : {}".format(k , v))

                dico2 = dico.copy() - le resultat de la copie normal est identique à la copie pour une liste

                
                
                une  fonction dont les parametres(parametre nomé) sont des dictionaire 
                def fonction_b (**parametres):
                    print(**parametres)

                fonction_b(p=23 , ti="qwertyuuuui")




"""