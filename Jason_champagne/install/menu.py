import tkinter


#add_checkbutton()
#add_radiobutton()
#add_separator()
def show_about():
    about_window=tkinter.Toplevel(app)
    about_window.title("À propos")
    lb = tkinter.Label(about_window, text="c'est moi")
    lb.pack()
    #about_window.mainloop()

#création de la fenetre plus fenetrage
app = tkinter.Tk()
app.title("Menu25_Tk")
app.geometry("640x480")

#widgets


mainmenu = tkinter.Menu(app)

first_menu = tkinter.Menu(mainmenu, tearoff=0)
first_menu.add_command(label="öption1")#command = <nom de la fonction pour rajouter des command>
first_menu.add_command(label="öption2")
first_menu.add_command(label="Quiter", command = app.quit)



second_menu = tkinter.Menu(mainmenu , tearoff=0)
second_menu.add_command(label="option1")
second_menu.add_command(label="option2")
second_menu.add_command(label="A propos", command=show_about)









mainmenu.add_cascade(label="Premier", menu=first_menu)
mainmenu.add_cascade(label="second", menu=second_menu)




app.config(menu=mainmenu)
app.mainloop()