import tkinter

"""
StringVar() : str
IntVar()    : int
DoubleVar() : float
BooleanVar() : bool : 1= true et
"""
#l'observeur
#def update_label(*args):
#    var_label.set(var_entry.get())

def update_l(*args):
    if var_e.get():
        var_label_ev.set("C'est un mec")

    else:
        var_label_ev.set("C'est une meuf")


app = tkinter.Tk()
app.geometry("800x600")
app.title("Variable_controle_TK")






#widgets............


#var_label = tkinter.StringVar()#déclaration de la variable tkinter
#label1 = tkinter.Label(app, text="", textvariable= var_label) #width = 20, textvarible : remplace le parametre text
##var_label.set("coucou") # var_label.get:pour l'avoir


#var_entry = tkinter.StringVar()
#var_entry.trace("w",update_label) #cette ligne mais en place un getteur,(<mode de lecture> ,<le nom de la fonction qui sera notifié quand on modifie la variable>)
# u pour la supression, w: gete la la modification, r: à chaque fois que sera lue
#entry = tkinter.Entry(app, textvariable = var_entry)

var_e = tkinter.IntVar()
var_e.trace("w",update_l )
radio1 = tkinter.Radiobutton(app, text="Homme" , value =1 , variable = var_e)
radio2 = tkinter.Radiobutton(app, text="Femme", value =0   , variable = var_e)

var_label_ev = tkinter.StringVar()
label_gender = tkinter.Label(app, textvariable= var_label_ev)


label_gender.pack()
radio1.pack()
radio2.pack()
#entry.pack()
#label1.pack()

#boucle principal
app.mainloop()