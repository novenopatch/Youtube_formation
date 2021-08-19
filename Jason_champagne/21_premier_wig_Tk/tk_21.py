"""
<nom_variable> = <nom_widget>(<widget_parent>, <parametre>...)
"""
import tkinter
app= tkinter.Tk()

app.title("test1 Tk")

screen_x = int(app.winfo_screenwidth())
screen_y = int(app.winfo_screenheight())
window_x = 800
window_y = 600
position_x = (screen_x // 2) - (window_x // 2)
position_y = (screen_y // 2) - (window_y // 2)
geo = "{}x{}+{}+{}".format(window_x, window_y, position_x, position_y)
app.geometry(geo)


#label_welcome = tkinter.Label(app, text="Bienvenue !")# mettre justify au lieu de text
#message_welcome = tkinter.Message(app, text="Bienvenue !")#message sur plusieur ligne
#entry_name = tkinter.Entry(app) #la taille du champ se modifie par:
#entry_name = tkinter.Entry(app, width= <valeur entier>)
#entry_name = tkinter.Entry(app, show="*")#cela remplace par l'element entre les guillemet
#entry_name = tkinter.Entry(app, exportselection= 0)#empeche la saisie de rester dans le presse papier 
#button_k = tkinter.Button(app, text="Ok") #<width> et <height> permet de définir la taille , <command> pour appeller des fonction pour faire des genre de log(command =<nom_de_la_fonction>)





#button_k.pack
#entry_name.pack()
#message_welcome.pack()
#label_welcome.pack()#cette ligne gère le positionement
app.mainloop()