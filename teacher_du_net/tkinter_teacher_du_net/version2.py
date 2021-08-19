import tkinter as tk
from tkinter import ttk
#pour les icones c'est www.iconefinder.com
class CoureurApp():
    def __init__(self,master):
        self.girlfriend = 3
        

        self.status_lbl = ttk.Label(master, foreground="#ff0000", font=("courier",18,"bold italic" ))#, background="black")
        self.add_girlfriend_btn = ttk.Button(master,text="j'ai une nouvelle copine",command= self.add_copine)
        self.remove_girlfriend_btn = ttk.Button(master,text="j'ai perdu une copine",command= self.remove_copine)

        self.update_statut_lbl(self.girlfriend)
        self.status_lbl.pack() 
        self.add_girlfriend_btn.pack()  
        self.remove_girlfriend_btn.pack() 

    def add_copine(self):
        self.girlfriend +=1
        self.update_statut_lbl(self.girlfriend)

    def remove_copine(self):
        if(self.girlfriend>0):
            self.girlfriend -=1
            self.update_statut_lbl(self.girlfriend)
            

    def update_statut_lbl(self, girlfriendCount):
        self.status_lbl.config( text ="Nombre de copines actuel: {}".format(str(girlfriendCount)))


def main():
    root = tk.Tk()
    root.title("coureur de jupon")
    style = ttk.Style()
    style.theme_names()
    #style.theme_use("aqua")
    app = CoureurApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()