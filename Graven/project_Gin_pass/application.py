import  sys
import os
try:
    import pwd
except ImportError:
    pass
from tkinter import filedialog
from tkinter import*
from tkinter import messagebox
from random import randint, choice

import string
import datetime
import getpass


password_entry_t = ""
color = "#4065A4"
width_img = 200
height_img = 200

window_x = 780
window_y = 480

file_bool = False


class Application:
    
    
    def __init__(self):

        

        self.window = Tk()
        self.window.title("JIN_PASS_V1.0")
        
        screen_x = int(self.window.winfo_screenwidth())
        screen_y = int(self.window.winfo_screenheight())
        position_x = (screen_x // 2) - (window_x // 2)
        position_y = (screen_y // 2) - (window_y // 2)

        geo = "{}x{}+{}+{}".format(window_x, window_y, position_x, position_y)
        self.window.geometry(geo)
        #self.window.geometry("720x480")
        self.window.minsize(720,480)
        self.window.config(bg= color)
        
        #definition Frame (la premiere frame)
        self.frame = Frame(self.window, bg=color)
        self.frame.pack(expand=YES)
        
        #canvas
        self.image = PhotoImage(file="cap.png").zoom(39).subsample(32)
        self.canvas = Canvas(self.frame, width=width_img, height=height_img, bg =color, bd=0, highlightthickness=0)
        self.canvas.create_image(width_img/2, height_img/2, image=self.image)
        self.canvas.grid(row=0,column=0,sticky=W)
        


        #definition frame_2 conteant les autre widgets
        self.right_frame = Frame(self.frame, bg=color)
        self.right_frame.grid(row=0,column=2, sticky=W)

        
        #il appelle les autre widgets la methode creatrice des widgets contenue dans frame 2
        self.create_widgets()
        self.fsaveFile()


    def fsaveFile(self):
        global  file_bool
        if not file_bool:
            files = filedialog.asksaveasfile(initialdir="/home/", title="Select file",
                                                 filetypes=(("png files", "*.png"), ("jpeg files", "*.jpg"), (
                                                 "all files",
                                                 "*.*)")))
            file_bool = True
            self.file = files
        else:
            pass
       
    
    def create_widgets(self):
        self.menu_app()
        #self.create_test_label()
        self.create_label_titre()
        self.create_password_entry()
        self.create_password_generator_buton()
        

    #def create_test_label(self):
        #label_text = Label(self.right_frame, text="Cocher pour enregistre")
        #label_text.pack(side = LEFT, anchor =W, pady= 20,padx=5)
        #check = Checkbutton(self.right_frame)
        #check.pack(side = LEFT,anchor =W, pady= 20, padx=5)

    def create_label_titre(self):
        label_title = Label(self.right_frame, text="Mot de passe", font=("Helvetica",20), background=color,fg="white")
        label_title.pack()

    def create_password_entry(self):
        global password_entry_t
        password_entry_t = StringVar()
        password_entry = Entry(self.right_frame, textvariable = password_entry_t , font=("Helvetica",20), bg="white",fg=color)
        password_entry.pack()
        
    def create_password_generator_buton(self):
        generate_password_button = Button(self.right_frame, text="Generer", font=("Helvetica",20),
         bg=color,fg="white",command= self.generateur_password_r)
        generate_password_button.pack()#fill=X)


    def menu_app(self):

        #bar de menu
        menu_bar = Menu(self.window)
        #premier menu(menu ficher)
        file_menu = Menu(menu_bar,tearoff=0)
        file_menu.add_command(label="Nouveau", command= self.generateur_password_r)
        file_menu.add_command(label="Quiter", command=self.window.quit)

        second_menu = Menu(menu_bar , tearoff=0)
        second_menu.add_command(label="A propos", command= self.afficher_apropos_window)
        
        menu_bar.add_cascade(label="Ficher", menu=file_menu)
        menu_bar.add_cascade(label="aide", menu=second_menu)

        #ajouter le menu
        self.window.config(menu=menu_bar)


    #foncton qui genere le putain de pass
    
    def generateur_password_r(self ,pass_min=10, pass_max=14, ponctuation=True):
        global password_entry_t
        global file_bool

        
        if pass_min==6 and pass_max==12 and ponctuation:#in default
            all_chars = string.ascii_letters + string.punctuation + string.digits
            password = "".join(choice(all_chars) for i in range(randint(pass_min,pass_max)))
        elif not ponctuation:
            all_chars = string.ascii_letters + string.digits
            password = "".join(choice(all_chars) for i in range(randint(pass_min,pass_max)))
        else:
            all_chars = string.ascii_letters + string.punctuation + string.digits
            password = "".join(choice(all_chars) for i in range(randint(pass_min,pass_max)))

        x = len(password)
        espace = x * " "
        temps = str(datetime.datetime.now())
        at = "at:--->"
        l = "\n"
        """
        def createFile():

           files = filedialog.asksaveasfile(initialdir="/home/", title="Select file",
                                                 filetypes=(("png files", "*.png"), ("jpeg files", "*.jpg"), (
                                                 "all files",
                                                 "*.*)")))  # filedialog.askopenfilename.......#pour ouvrir autre ficher
           #print(files)
           file_bool = True
            return files
            """


        def saveFile(files):
            try:
                with  files:
                    # with open("old_passwords.txt", "a+") as files: #files:
                    files.write(password + espace + at + temps + 2 * l)

            except:
                messagebox.showwarning("Une erreur inatendue", "Veillez ferme cette fenetre et recommencer")
                with open("old_passwords.txt", "a+") as files:
                    files.write(password + espace +  at + temps  + 2*l)
                    files.close()
            finally:
                files.close()
        password_entry_t.set(password)

        saveFile(self.file)
       


        
    def afficher_apropos_window (self):
        a_propos=Toplevel(self.window)
        a_propos.geometry("600x400")
        a_propos.minsize(600,400)
        a_propos.maxsize(700,500)
        a_propos.title("À propos")
        try:
            top = sys.platform# know platforrm
        except:
            top=""
            print("gggggggr")
        if top == "linux":
            var_u = pwd.getpwuid(os.getuid())#know password user name on linux
            tor =  "hello, user: " + var_u.pw_name
            texte= tor + "\n je me nomme HOMAWOO JOSEPH.\n cet petit logiciel est encore au stade de developpement.\n j'y ajouterai de nouvelle fonctionalite par la suite. \n merci "

        else:
            #var_u = pwd.getpwuid(os.getuid())#know password user name on linux
            tor =  "hello, user: " + os.getlogin()
            texte= tor + "\n je me nomme HOMAWOO JOSEPH.\n cet petit logiciel est encore au stade de developpement.\n j'y ajouterai de nouvelle fonctionalite par la suite. \n merci "
        
        texte_v = StringVar()
        texte_v.set(texte)
        lb = Label(a_propos, textvariable = texte_v)
        lb.pack()
        #return "%s@%s" % (pwd.getpwuid(os.getuid()).pw_name, platform.node())

        #return "%s@%s" % (getpass.getuser(), platform.node())
        a_propos.mainloop()
    