#coding:utf-8

# pour afficher l'aide help(str)

"""
les méthode de chaine travaille sur une copie , et pas sur la chaine elle-meme 

str.upper(), str.lower(), str.capitalize(), str.title() == maj deb mo
str.center(<largeur>, {caratère de remplisassge ps obligtoir exempl:"-"})

str.strip(): il enlève l'epace au debut et apres le str

str.find(<chaine>, <debut>, <fin>): 2 dernier partr snt op obliga 
str.index(<chaine>, <debut>, <fin>): 2 d p option/ lui s'il n trouve pas le mots il lève une erreur donc il faut la gére 

str.replace(<ancienne> , <nouvelle> , <occurence (op)>): elle fait du remplacement

str.split("<l'element séparateur exemple si |>")

str.isalpha(), str.isdigit() , str.isdecimal(). str.isnumeric() , str.isalphanum(),
 
str.islower(), str.isupper()

str.isidentifier(), str.iskeyword

chat = "Thor"

if "or" in chat :
    print("Trouvé")
else :
    print("Nom troué")
#la méthode décripte la haut permet de faire de petit recherche




"""

#ma_chaine = "Hello word"

#ma_chaine = ma_chaine.capitalize()
#print(ma_chaine)