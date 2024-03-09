from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello_world():
    return "<p>Hello !</p>"

class WorkWT:
    @staticmethod
    @app.route('/TextToSpeach', methods=['POST'])
    def text_to_speech():
        data = request.get_json()
        speech = data.get("text", "")
        textLanguage = data.get("textLanguage", "")
        textToLanguage = data.get("textToLanguage", "")
        # Zpracování textu na zvuk
        # ...
        Response["speech"]        =AWS_TextToSpeech()
        Response["speechLanguage"]=AWS_speechLanguage()
        Response={"speech": "1230809481092834", "speechLanguage": "EN"}
        return Response

    @staticmethod
    @app.route('/SpeachToText', methods=['POST'])
    def speech_to_text():
        data             = request.get_json()
        speech           = data.get("speech", "")
        speechLanguage   = data.get("speechLanguage", "")
        speechToLanguage = data.get("speechToLanguage", "")
        # Zpracování zvuku na text
        # ...

        Response["text"]         = AWS_SpeechToText()
        Response["textLanguage"] = AWS_textLanguage()
        Response={"text":"Some text", "textLanguage": "EN"}	
        return Response

    @staticmethod
    @app.route('/SymbolsToText', methods=['POST'])
    def symbols_to_text():
        data = request.get_json()
        symbols = data.get("symbols", "")
        
        # Zpracování symbolů na text
        # ...
        Response["text"]        =AWS_SymbolsToText()
        Response["textLanguage"]=AWS_textLanguage()
        Response={"text":"Some text", "textLanguage": "EN"}
        return Response

    @staticmethod
    @app.route('/TextToSymbols', methods=['POST'])
    def text_to_symbols():
        data = request.get_json()
        text = data.get("text", "")
        # Zpracování textu na symboly
        # ...
        Response["image"]=AWS_TextToSymbols()
        Response={"image":"1230809481092834"}
        return Response

controllerW = WorkWT()

if __name__ == "__main__":
    app.run(port=4000)
