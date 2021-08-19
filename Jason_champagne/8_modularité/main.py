#coding:utf-8
#il suffit alors de faire un import du nom du ficher module
#pour faire l'appel du ficher bah methode normale
#import mod
#mod.tom()
#si le ficher du module est dans un sous dossier par exemple le nom du dossier est tom et ficher du module est modalo pour faire le import on doit faire: import tom.modalo
#pour le reste on faite comme avant avec de petit changement:
#on peut aussi faire : import <nom_du_dossier>.<nom_du_ficher_du_module> as <nom_du ficher_du_module>
#grace à l'import designé précédement pour faire l'appel on à juste besoin de faire: <nom_du_ficher_du_module>.<nom_de_la_fonction> ce qui change c'est juste que l'on n'a plus à préciser le chemin vers le ficher du module (bah si j'ai bonne mémoire au moment où j'ecrit ces ligne je n'ai pas encors essayé la partie compliqué de mes écrit )
"""
pour tester un module du programme
dans le fichers du module
if__name__=="__<nom_du_ficher_main(le_lanceur_quoi)>__":
    <nom_de_la_fonction> #genre on fait appel des fonction contenue dans le module
    pour faire cela il suffirat alors de lancer le ficher py du module
"""