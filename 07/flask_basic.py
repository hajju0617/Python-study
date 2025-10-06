from flask import Flask
import os
os.chdir("C:/Python-study/07")

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello Python</h1>"


'''
vscode에서 터미널로 실행 방법

1. cd C:\Python-study\07 입력.
2. $env:FLASK_APP = "flask_basic" 입력.
3. flask run 입력.
'''