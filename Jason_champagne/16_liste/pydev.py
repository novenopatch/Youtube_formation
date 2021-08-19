#coding:utf-8
################--liste--
"""
création1 : <nom de la variable > = list() <== celle-ci est vide

création2 : ma_liste = [] <= vide aussi

création3 : ma_liste = [0 , "tr"] <= contenant 0, "tr"

création4 : ma_liste = [0] * 10  <= à ca création elle contient alors 10 zéro , on peut faire ca avec n'importe quelle contenance

création5 : ma_liste = range(20) <= elle mais dans la liste 0,1.... juska 20


                  
                  
                  
                  
                  
                  
                  
                  ########----affichage----

print(ma_liste[:3]): les trois premiers éléments

print(ma_liste[3:]): les trois derniers éléments

print(ma_liste[3]): indice 3

print(ma_liste[-3]) : 3m element en partant de la fin

print(ma_liste [:]): affiche tout

print(liste[A:B]) = indice A jusqua b(le b est exclu)


for valeur in ma_liste:
    <instruction>

for liste in enumerate(ma_liste):


for k , v in enumerate(ma_liste)   

len(<liste>) : elle retourne la taille

idice = num de l'élément

len(nom_de la_liste): donne la taille  maximal

if "element_que_l'_on_cherche" in <nom_de_la_liste> :
    <instructions>
else:

print(liste_X.index("<element de la liste X>")) : listN.index.("") affiche lindice dun element de la liste

liste_X.sort() : si la liste est constitué par exemple de seulement des str on peut la trié par ordre croissant

liste.reverse() : il inverse la liste

list.count("<element a compter>"): il compte les element

list_X.clear ou list_X[:] = []

passer d'une liste à une chaine: les instructions sont en dessous

list_X = ["Bonjour","à","tous"]

phrase = "<séparateur exemple: "-">".join(list_X)












                                ################-probleme avec les liste :

liste1 = ["blue", "Nokia" ,"ZTE"]

liste2 = liste1 #le normalement on s'attent à ce que la liste2 soit une copie de la liste mais non cela ne se passe comme cela, on lie en faite les deux liste sont en faite genre toute modification de la liste2 se répercute sur la liste1
 la methode pour faire une copie de liste est alors:
 import copy
 list2 = copy.deepcopy(liste1)
concaténation liste:
1) list1.extend(liste2) == liste1 = liste1 + list2 = liste1 += liste2





                      #########--mod

liste_X[:2] =  ["",""]:il modifie les deux premiers élement par "" et ""

liste_X[:] = ["<l'élément avec lequelle on veut modifier>"] * len(liste_X)

liste_X.append("l_element_a_ajouter") : 

liste_X.insert(<numero_de_l_indiice> , "element à ajouter")

                       #################-----Supression----####

liste_X.remove("<lelement que lon veut suprimer>")


del liste_X[<numero de lindice>]



"""