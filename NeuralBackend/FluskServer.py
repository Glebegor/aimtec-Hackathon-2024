from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello !</p>"

@app.route('/form_example', methods=['POST'])
def handle_form():
    print(request.form.get('name'))
    print(request.form.get('age'))
    return request.form

@app.route('/TextToSpeach', methods=['POST'])
def handle_form():
    print(request.form.get('name'))
    print(request.form.get('age'))
    return request.form

@app.route('/SpeachToText', methods=['POST'])
def handle_form():
    print(request.form.get('name'))
    print(request.form.get('age'))
    return request.form

@app.route('/SymbolsToText', methods=['POST'])
def handle_form():
    print(request.form.get('name'))
    print(request.form.get('age'))
    return request.form





#parsing JSON
#
#