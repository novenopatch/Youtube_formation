#coding:utf-8
import sqlite3

connection = sqlite3.connect("base.db")
cursor = connection.cursor()

new_user = (cursor.lastrowid,"Kugar",500)
cursor.execute('INSERT INTO tt_users VALUES(?,?,?)', new_user)
#excecute:pour passer une variable unique
#executemany permet d'ajouter plusieur utilisateur en meme temp,pour se faire il suffirait de faire une liste contenant, les élement
connection.commit()
print("Nouvel utilisateur ajouté !")

connection.close()
