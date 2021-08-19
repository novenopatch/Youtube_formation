#coding:utf-8
import sqlite3

connection = sqlite3.connect("base.db")
cursor = connection.cursor()

my_username = ("jinjo",)
cursor.execute('SELECT * FROM tt_users WHERE user_name = ?', my_username)
resultat = cursor.fetchone()[1]
print(f"Le nom d'utilisateur est : {resultat}")



connection.close()