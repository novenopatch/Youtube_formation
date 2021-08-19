
import tkinter
from tkinter import messagebox #pour afficher des message d'erreur dans l'interface

"""
aulieu de showerror il y  aussi:
                                showinfo
                                showwarning
                                askquestion
                                askokcancel
                                askyesno
                                askretrycancel
"""

def show_modal_window():
    messagebox.showerror("ERREUR", "Un problème est survenu !")
app= tkinter.Tk()
app.title("Tkkkkkkkkkkkkkkkkkkkkkk")

screen_x = int(app.winfo_screenwidth())
screen_y = int(app.winfo_screenheight())
window_x = 800
window_y = 600
position_x = (screen_x // 2) - (window_x // 2)
position_y = (screen_y // 2) - (window_y // 2)
geo = "{}x{}+{}+{}".format(window_x, window_y, position_x, position_y)
app.geometry(geo)


check_widget = tkinter.Checkbutton(app, text="publier")
#check_widget = tkinter.Checkbutton(app, text="publier"),ofvalue= <>,onvalue<>
radio_w2 = tkinter.Radiobutton(app, text="Homme", value =1)
radio_w1 = tkinter.Radiobutton(app, text="Femme",value = 0)

scale_w = tkinter.Scale(app,from_=5 , to= 100)# par: tickinterval = <>

spin_w = tkinter.Spinbox(app,from_=1 , to=10)

lb = tkinter.Listbox(app)# cést une liste lb.insert(1, "<>")

btn = tkinter.Button(app, text="Déclencher une erreue", command= show_modal_window)



btn.pack()
lb.pack()
spin_w.pack()
scale_w.pack()
radio_w2.pack()
radio_w1.pack()
check_widget.pack()
app.mainloop()