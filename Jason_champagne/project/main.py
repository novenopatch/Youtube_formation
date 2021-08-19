import tkinter
import pygame

pygame.init()
window_x = 640
window_y = 480
window_resolution = (640, 480)

fenetre_p = tkinter.Tk() 

fenetre_p= pygame.display.set_mode(window_resolution)


pygame.display.set_caption("40_event")

fenetre_p.title("40_event")


screen_x = int(fenetre_p.winfo_screenwidth())
screen_y = int(fenetre_p.winfo_screenheight())


fenetre_p.resizable(width = False, height = False)

position_x = (screen_x // 2) - (window_x // 2)
position_y = (screen_y // 2) - (window_y // 2)

geo = "{}x{}+{}+{}".format(window_x, window_y, position_x, position_y)





launched = True

while launched :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    fenetre_p.geometry(geo)
    fenetre_p.mainloop()