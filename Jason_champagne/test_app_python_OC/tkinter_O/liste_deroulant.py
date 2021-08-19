from tkinter import*


fenetre=Tk()
liste = Listbox(fenetre) 
liste.pack()
#On insère ensuite des éléments. 
# La méthode insert prend deux paramètres : 
# 1. la position à laquelle insérer l'élément ; 
# 2. l'élément même, sous la forme d'une chaîne de caractères. 
# Si vous voulez insérer des éléments à la fin de la liste, utilisez la constante END définie par Tkinter : 
liste.insert(END, "Pierre") 
liste.insert(END, "Feuille") 
liste.insert(END, "Ciseau")

#Pour accéder à la sélection, utilisez la méthode curselection de la liste. 
# Elle renvoie un tuple de chaînes de caractères, chacune étant la position de l'élément sélectionné.
# Par exemple, si liste.curselection() renvoie ('2',), c'est le troisième élément de la liste qui est sélectionné (Ciseau en l'occurrence). 

fenetre.mainloop()