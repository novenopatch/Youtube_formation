from tkinter   import*

fenetre = Tk()
var_case = IntVar() 
case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case) 
case.pack()
var_case.get()



fenetre.mainloop()