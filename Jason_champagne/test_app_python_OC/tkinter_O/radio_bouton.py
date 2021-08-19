from tkinter import*


fenetre= Tk()

var_choix = StringVar() 
choix_rouge = Radiobutton(fenetre, text="Rouge", variable=var_choix, value="rouge") 
choix_vert = Radiobutton(fenetre, text="Vert", variable=var_choix, value="vert") 
choix_bleu = Radiobutton(fenetre, text="Bleu", variable=var_choix, value="bleu") 
choix_rouge.pack() 
choix_vert.pack() 
choix_bleu.pack()
#var_choix.get()
fenetre.mainloop()