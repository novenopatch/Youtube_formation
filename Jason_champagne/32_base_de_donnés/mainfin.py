#coding:utf-8
import sqlite3

try:
    connection = sqlite3.connect("base.db")#connexion a la base de donné si elle nést pas rpésent elle est crée
    cursor = connection.cursor()#initilise un curseur

    req = cursor.execute('SELECT * FROM tt_users')#met les resultat du curseur dans  la variable req
    #si l'on chercher a affiché un utilisateur dans la base de données qui n'exite pas un message d'erreur n'est pas générer juste une requete sans réponse (logique)

    for row in req.fetchall():#la mehode fetchall permet d'affiche la base de donné
        print(row[1]) 
        # row simple affiche chaque valeur contenue dans req,[<1> affiche la premier valeur de l'indice ]
        # exemple:list_W = [(999, 9),(789787,"t")]
except Exception as e:
    print("[ERREUR]", e)
    connection.rollback()#cette commande sur la variable de la base de donné permet de faire u retour au commit précédent ,ici elle esg executé en cas d'erreur cést sont domaine d'usage.


finally:
connection.close()#ferme la base de donnés

#print(req.fetchall())
