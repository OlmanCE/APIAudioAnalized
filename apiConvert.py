from flask import Flask, request, jsonify
import os
import subprocess
import tempfile
import speech_recognition as sr

app = Flask(__name__)

def convert_opus_to_wav(input_file_path, output_file_path):
    try:
        subprocess.run(['ffmpeg', '-i', input_file_path, output_file_path], check=True)
        return output_file_path
    except Exception as e:
        print(f"Error al convertir el archivo: {str(e)}")
        return None

def transcribe_wav_to_text(wav_file_path, language="es-ES"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language=language)
            return text
        except sr.UnknownValueError:
            return "Error: El audio no pudo ser entendido."
        except sr.RequestError as e:
            return f"Error: No se pudo solicitar resultados del servicio de reconocimiento de voz; {e}"

@app.route('/convert-and-transcribe', methods=['POST'])
def convert_and_transcribe():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    
    with tempfile.TemporaryDirectory() as tmpdirname:
        input_path = os.path.join(tmpdirname, file.filename)
        output_wav_path = os.path.join(tmpdirname, "output.wav")
        
        file.save(input_path)
        
        converted_path = convert_opus_to_wav(input_path, output_wav_path)
        if converted_path:
            text = transcribe_wav_to_text(converted_path)
            return jsonify({"transcription": text})
        else:
            return "Error converting file", 500

if __name__ == '__main__':
    app.run(debug=True)
