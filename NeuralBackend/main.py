from flask import Flask, request, jsonify
import boto3

session = boto3.Session()
polly = session.client("polly", "eu-west-1")
response = polly.synthesize_speech(Text="Hello world!", OutputFormat="mp3",
                                        VoiceId="Joanna")

# boto3.client(
#     's3',
#     aws_access_key_id=os.getenv("aws_access_key_id"),
#     aws_secret_access_key=os.getenv("aws_secret_access_key"),
# )



app = Flask(__name__)

# Define a simple route
@app.route('/')
def hello():
    return 'Hello, World!'

# Example route for handling POST requests
@app.route('/workWT/TextToSpeech', methods=['POST'])
def text_to_speech():
        data = request.get_json()
        text = data.get('text', '')
        text_language = data.get('textLanguage', '')
        text_to_language = data.get('textToLanguage', '')

        return jsonify({"speech": "123120-381-283091273981762", "speechLanguage": "En"})

@app.route('/workWT/SpeechToText', methods=['POST'])
def speech_to_text():
        data = request.get_json()
        text = data.get('speech', '')
        text_language = data.get('speechLanguage', '')
        text_to_language = data.get('speechToLanguage', '')

        return jsonify({"speech": "123120-381-283091273981762", "speechLanguage": "En"})

if __name__ == '__main__':
    app.run(debug=True)
