#coding:utf-8
import sqlite3

connection = sqlite3.connect("base.db")
cursor = connection.cursor()

req = cursor.execute('SELECT * FROM tt_users')

#print(req.fetchall())

for row in req.fetchall():
    print(row[1]) # row simple affiche chaque valeur contenue dans req,[<1> affiche la premier valeur de l'indice ]

connection.close()

# exemple:list_W = [(999, 9),(789787,"t")]
