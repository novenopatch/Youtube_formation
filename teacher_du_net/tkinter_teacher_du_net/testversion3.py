import tkinter as tk
from tkinter import ttk

class TestApp():
    def __init__(self,master):
        self.label = ttk.Label(master, text="blablabla")
        self.label.pack()


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