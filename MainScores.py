from flask import Flask

from Score import get_score

app = Flask(__name__)
'''
in seperade console run:
linux
export FLASK_APP=MainGame.py
win"
set FLASK_APP=MainGame.py

'''
@app.route("/")
def index():
    html_str = "<html> <head> <title>Scores Game</title> </head> <body> <center>"
    html_str += get_score()
    html_str += "</center></body> </html>"

    return html_str




