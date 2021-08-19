import tkinter


app = tkinter.Tk()
app.geometry("640x480")
app.title("positionement_tk")

#widgets

#mainframe = tkinter.Frame(app, width=300, height=200, borderwidth=1)#cardre
#mainframe.pack()

#mainframel = tkinter.LabelFrame(app, text= "titre du cadre", width=300, height=200, borderwidth=1)#cardre nomé
#mainframeL.pack()

btn = tkinter.Button(app,text="Bienvenue,")


label = tkinter.Label(app, text="un Label")


ent = tkinter.Entry(app,)


#side="top" quand on ne spécifie aucun paramètre;bottom,right,left
#expand=1(bool fake, il ocupe tous l'espace ou pas)
#fill="y"  ou "x"  ou "both" ou "none", couplé avec side
#marge: padx=<int> , pady=<>, marge interne ipadx = <>,ipady = <>


#label.grid() #positionement sous forme Tableau
# . grid(row=<> , colum= <>) 
# columnpan=2<pour que ce que l'on veut occupe 2 collone en meme temps et aussi rowspan= <> pour fair que l'element occupe plusieur ligne 
#sticky="se" #pour ce qui de l'oriention  n(nord), s(sud),e(est),w(ouest)

#label.place(x=10, y=10)
#pour un placement plus municieux
#relx , rely , pour les placement relatif

#le formateur préconise l'usage de frame pour gérer les groupe d'élement
label.pack()
ent.pack()
btn.pack()
app.mainloop()