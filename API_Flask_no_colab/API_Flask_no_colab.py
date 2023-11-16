-- curso realizado pela plataforma dio --
-- instalar a biblioteca "flask_ngrok" --
!pip install flask_ngrok

-- importar as bibliotecas --
import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import request, jsonify, Flask
import random as rk

-- nome do pacote de aplicativos e disponibilizar aplicativo Flask ao executar --
app = Flask(__name__) #the name of the application package
run_with_ngrok(app)

-- criar uma entrada para a API que estará na forma de um dicionário ou (JSON) --
d = {
    "name": "Nikola", 
    "surname": "Tesla", 
    "idade": 60
      }

-- roteamento de aplicativo --
@app.route("/") #code to assign HomePage URL in our app to function home.

def home():
  '''
  The entire line below must be written in a single line.
  '''
  return "<marquee><h3> TO CHECK IN PUT ADD '/input' TO THE URL AND TO CHECK OUT PUT ADD '/output' TO THE URL.</h3></marquee>"

--  receber a entrada e atribuir uma rota de aplicativo separada à função --
@app.route("/input") #code to assign Input URL in our app to function input.

def input():
  return jsonify(d) # "d" is the dictionary we defined

-- página de saída --
@app.route('/output', methods=['GET','POST']) #output page

def predJson():
 pred = r.choice(["positive","negative"])
 nd = d # our input
 nd["prediction"]=pred
 return jsonify(nd)

app.run()
