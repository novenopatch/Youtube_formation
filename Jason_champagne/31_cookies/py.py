import cgi

import http.cookies

#import datetime
import os
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) #règle le probleme d'ascent
"""
expires =
path =
comment
domain
secure
version
httponly
Set-Cookie : pref_lang = fr;

Sat, jj-mm-yy 12:45:66
create:
expiration = datetime.datetime.now() + datetime.timedelta(days=365)
expiration = expiration.strftime("%a, %d-%b-%Y %H:%M:%S")

my_cookie = http.cookies.SimpleCookie()
my_cookie ["pref_lang"] = "fr"
my_cookie ["pref_lang"] ["expires"] = expiration
my_cookie ["pref_lang"] ["httponly"] = True

print(my_cookie.output())

"""





print("Content-type: text/html; charset=utf-8 \n")
html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title> Une page web avec python et HTML !</title>
</head>
<body>
    <h1>Cookies avec Python</h1>

    """
print(html)

#partie récupération
"""
1)
if "HTTP_COOKIE" in os.environ:
    print(os.environ["HTTP_COOKIE"])
else :
    print("HTTP_COOKIE n'existe pas")
"""
try:
    user_lang = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
    print(user_lang["pref_lang"].value)
except(http.cookies.CookieError, KeyError):
    print("Non trouvé")

#fin parte recup
print("<p> Bonjour l'olo étanche h!</p>")

html = """
</body>
</html>
"""
print(html)