import tkinter as tk

girlfriend_nbr= 3

def add_copine():
    global girlfriend_nbr
    girlfriend_nbr +=1 
    statut_lbl["text"] = "Nombre de copines" + str(girlfriend_nbr)


def remove_copine():
    global girlfriend_nbr
    girlfriend_nbr -=1 
    statut_lbl["text"] = "Nombre de copines" + str(girlfriend_nbr)
    



root = tk.Tk()

root.title("coureur de jupon")

statut_lbl = tk.Label(root,text="Nombre de copines: 3")
add_girlfriend_btn = tk.Button(root,text="j'ai une nouvelle copine" , command= add_copine)
remove_girlfriend_btn = tk.Button(root,text="j'ai perdu une copine", command=remove_copine)

statut_lbl.pack()
add_girlfriend_btn.pack()
remove_girlfriend_btn.pack()


root.mainloop()