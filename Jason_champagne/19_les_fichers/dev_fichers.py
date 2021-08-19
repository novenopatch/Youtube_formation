"""
Modes d'ouverture:  r (lecture seule)
                    w (écriture remplacement)
                    a (écriture avec ajout en fin de ficher )
                    x (lecture et écriture)
                    r+ (lecture/ecriture dans un meme ficher)

"""

"""
 fic = open("dic.txt", "r")

 print(fich.read()) #elle essaye de lire tout le ficher

 line = fic.readline()# cette méthode lit le ficher par ligne
 print(line)
 line = fic.readlines()#il récupère tout le reste du ficher sous forme de liste


 fic.close()

 whith open("dic.txt", "r") as fic:
    content = fic.read()
    #avec cette synthaxe pas besoin de fermé le ficher

"""

"""
pour l'écriture
with open("dic.txt", "a") as fic :
          nombre = "\n test \n"
          fic.write(nombre)
"""

"""
        enregistrement de l'objet en binaire:
        import pickle
        class Player:
            def __init__(self,name,level):
                self.name = name
                self.level = level
            def whomi(self):
                print("{} ({})".format(self.name, self.level))

        p1 = Player("jinjo" , 20)

        with open("Player.data", "wb") as fic:
            record = pickle.Pickler(fic)
            record.dump(p1)

        pour la récupération:

        with open("Player.data", "rb") as fic:
            get_record = pickle.Unpickler(fic)
            player_one = get_record.load() #ici l'object est alors enregistrer dans la variable créé et nommé player_one

        
"""
