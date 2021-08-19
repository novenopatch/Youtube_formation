#codin:utf-8

import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

print("Content-type: text/html; charset=utf-8 \n")
html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title> Une page web avec python et HTML !</title>
</head>
<body>
    <h1>BIENVENUE sur la page de resulat</h1>

    """
print(html)

try :
    if form.getvalue("username"):
        username = form.getvalue("username")
        print(f"<p> Bonjour {username} !</p>")
        print("<script>alert('ok')</script>")#c du javascript
    else:
        raise Exception("Pseudo non transmis")
except:
    print("<p>Pseudo non transmis </p>")

html = """

</body>
</html>
"""
print(html)