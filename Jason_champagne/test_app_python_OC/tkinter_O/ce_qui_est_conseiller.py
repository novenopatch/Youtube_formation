from tkinter import * 

class Interface(Frame):
    """Notre fenêtre principale. 
Tous les widgets sont stockés comme attributs de cette fenêtre."""
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs) 
        self.pack(fill=BOTH)
        self.nb_clic = 0 
        # Création de nos widgets
        self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")
        self.message.pack()
        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")
        self.bouton_cliquer = Button(self, text="Cliquez ici", fg="red", command=self.cliquer)
        self.bouton_cliquer.pack(side="right")
    def cliquer(self):
        """Il y a eu un clic sur le bouton. On change la valeur du label message."""
        self.nb_clic += 1
        self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)
fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()
#Dans l'ordre : 
# 1. On crée une classe qui contiendra toute la fenêtre. Cette classe hérite de Frame, c'est-à-dire d'un cadre Tkinter. 
# 2. Dans le constructeur de la fenêtre, on appelle le constructeur du cadre et on pack (positionne et affiche) le cadre. 
# 3. Toujours dans le constructeur, on crée les différents widgets de la fenêtre. On les positionne et les affiche également. 
# 4. On crée une méthode bouton_cliquer, qui est appelée quand on clique sur le bouton_cliquer. Elle ne prend aucun paramètre. Elle va mettre à jour le texte contenu dans le label self.message pour afficher le nombre de clics enregistrés sur le bouton. 
# 5. On crée la fenêtre Tk qui est l'objet parent de l'interface que l'on instancie ensuite. 
# 6. On rentre dans la boucle mainloop. Elle s'interrompra quand on fermera la fenêtre. 
# 7. Ensuite, on détruit la fenêtre grâce à la méthode destroy.
