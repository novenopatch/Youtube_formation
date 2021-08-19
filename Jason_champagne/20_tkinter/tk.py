#coding:utf-8

import tkinter
#from tkinter import *

fenetre_p = tkinter.Tk() #elle crée la fenetre principale
fenetre_p.title("test1")
#fenetre_p.minsize(640, 480)#logigement la fenetre sassfiche en taille minimal

#fenetre_p.maxsize(1280, 720)

#geometry("XxY+0+0")
#fenetre_p.geometry("800x600")


"""
#centre la fenetre:         
                        position_x = (largeur_ecran // 2) - (largeur_fenetre // 2)
                        position_y = (hauteur_ecran // 2) - (largeur_fenetre // 2)
 exemple de geometrie sans le facteur centrage: 
                                            fenetre_p.geometry("800x600+100+10")
"""
#niveau code : """"
screen_x = int(fenetre_p.winfo_screenwidth())
screen_y = int(fenetre_p.winfo_screenheight())
window_x = 800
window_y = 600

position_x = (screen_x // 2) - (window_x // 2)
position_y = (screen_y // 2) - (window_y // 2)

geo = "{}x{}+{}+{}".format(window_x, window_y, position_x, position_y)

fenetre_p.geometry(geo)

#fenetre_p.positionfrom("user")#voir la position

#fenetre_p.sizefrom("user")#voir la taille

#fenetre_p.resizable(width = False, height = False)# permet de controler le redimentionement


fenetre_p.mainloop()#boocle qui garde la febetre oouverte