from tkinter import*
fenetre = Tk()
#Il existe plusieurs widgets qui peuvent contenir d'autres widgets. 
# L'un d'entre eux se nomme Frame. C'est un cadre rectangulaire dans lequel vous pouvez placer vos widgets... ainsi que d'autres objets Frame si besoin est.
#  Si vous voulez qu'un widget apparaisse dans un cadre, utilisez le Frame comme parent à la création du widget : 

cadre = Frame(fenetre, width=768, height=576, borderwidth=1) 
cadre.pack(fill=BOTH) 
message = Label(cadre, text="Notre fenêtre") 
message.pack(side="top", fill=X)

#Comme vous le voyez, nous avons passé plusieurs arguments nommés à notre méthode pack. 
# Cette méthode, je vous l'ai dit, sert à placer nos widgets dans la fenêtre (ici, dans le cadre). 
# En précisant side="top", on demande à ce que le widget soit placé en haut de son parent (ici, notre cadre). 
# Il existe aussi l'argument nommé fill qui permet au widget de remplir le widget parent, 
# soit en largeur si la valeur est X, soit en hauteur si la valeur est Y, soit en largeur et hauteur si la valeur est BOTH. 
# D'autres arguments nommés existent, bien entendu. Si vous voulez une liste exhaustive, 
# rendez-vous sur le chapitre consacré à Tkinter dans la documentation officielle de Python. 
# Une partie est consacrée au packer et à la méthode pack. 
# Notez qu'il existe aussi le widget Labelframe, un cadre avec un titre, ce qui nous évite d'avoir à placer un label en haut du cadre. 
# Il se construit comme un Frame mais peut prendre en argument, à la construction, le texte représentant le titre : cadre = Labelframe(..., text="Titre du cadre")


fenetre.mainloop()
