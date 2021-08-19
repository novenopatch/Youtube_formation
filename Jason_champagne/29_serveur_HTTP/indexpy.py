#coding = utf-8
import cgi

print("Content-type: text/html; charset=utf-8 \n")

html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title> Une page web avec python et HTML !</title>
</head>
<body>
    <h1>BIENVENUE</h1>
    <p>
        La balise p sert crée un paragraphe.
        <details>
            qwerty kandar avenger
        </details>
    </p>
</body>
</html>
"""
print(html)