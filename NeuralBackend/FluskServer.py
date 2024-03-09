from flask import Flask,request
#import requests as request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello !</p>"

@app.route('/form_example', methods=['POST'])
def form_example():
    print(request.form.get('name'))
    print(request.form.get('age'))
    return request.form

@app.route('/TextToSpeach', methods=['POST'])
#text vrati odpoved na zvuk 
def TextToSpeach():
    data = request.get_json()
    data["speach"]
    return data["speach"]

@app.route('/SpeachToText', methods=['POST'])
#zvuk a vrati text
def SpeachToText():
    data = request.get_json()
    data["text"]
    return data["text"]

@app.route('/SymbolsToText', methods=['POST'])
def SymbolsToText():
    data = request.get_json()
    data["text"]
    return data["text"]

@app.route('/TextToSymbols', methods=['POST'])
def TextToSymbols():
    data = request.get_json()
    data["symbols"]
    return data["symbols"]





#parsing JSON
#
#