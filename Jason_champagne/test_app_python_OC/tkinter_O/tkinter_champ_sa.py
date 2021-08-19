from  tkinter import*
fenetre = Tk()
var_texte = StringVar()
var_texte = "entrez un truc"
saisie = Entry(fenetre,textvariable=var_texte, width=40)
saisie.pack()
fenetre.mainloop()
