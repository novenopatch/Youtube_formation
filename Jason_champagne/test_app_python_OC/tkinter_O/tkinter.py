import tkinter

# On crée une fenêtre, racine de notre interface 
fenetre= tkinter.Tk()

# On crée un label (ligne de texte) souhaitant la bienvenue
# Note : le premier paramètre passé au constructeur de Label est notre 
#  interface racine
champ_label = tkinter.Label(fenetre,text="salut le monde !")
# On affiche le label dans la fenêtre
champ_label.pack()

fenetre.mainloop()

