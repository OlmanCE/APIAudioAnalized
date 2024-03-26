from flask import Flask, request, jsonify
import concurrent.futures
import os
import subprocess
import tempfile
import speech_recognition as sr

app = Flask(__name__)
# Se encarga de convertir un archivo OPUS a WAV
# se utiliza la librería FFmpeg para realizar la conversión de formatos de audio
# ademas se utiliza la librería subprocess para ejecutar FFmpeg desde Python y realizar la conversión
def convert_opus_to_wav(input_file_path, output_file_path):
    try:
        # subprocess.run se encarga de ejecutar FFmpeg y convertir el archivo OPUS a WAV 
        # asimilando el comando de terminal: ffmpeg -i input_file_path output_file_path
        subprocess.run(['ffmpeg', '-i', input_file_path, output_file_path], check=True)
        return output_file_path
    except Exception as e:
        print(f"Error al convertir el archivo: {str(e)}")
        return None
# Se encarga de transcribir un archivo de audio a texto
def transcribe_wav_to_text(wav_file_path, language="es-ES"):
    #se utiliza la librería SpeechRecognition de Python que consume el servicio de reconocimiento de voz de Google
    recognizer = sr.Recognizer()
    # Se utiliza el método record de la clase Recognizer para leer el archivo de audio 
    with sr.AudioFile(wav_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            # Se utiliza el método recognize_google de la clase Recognizer para transcribir el audio a texto
            text = recognizer.recognize_google(audio_data, language=language)
            return text
        except sr.UnknownValueError:
            return "Error: El audio no pudo ser entendido."
        except sr.RequestError as e:
            return f"Error: No se pudo solicitar resultados del servicio de reconocimiento de voz; {e}"

@app.route('/convert-and-transcribe', methods=['POST'])
def convert_and_transcribe():
    files = request.files.getlist('file')
    results = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_file = {executor.submit(process_audio_file, file): file for file in files}
        for future in concurrent.futures.as_completed(future_to_file):
            results.append(future.result())

    return jsonify(results)

def process_audio_file(file):
    with tempfile.TemporaryDirectory() as tmpdirname:
        input_path = os.path.join(tmpdirname, file.filename)
        output_wav_path = os.path.join(tmpdirname, "output.wav")
        
        file.save(input_path)
        
        converted_path = convert_opus_to_wav(input_path, output_wav_path)
        if converted_path:
            text = transcribe_wav_to_text(converted_path)
            return {"filename": file.filename, "transcription": text}
        else:
            return {"filename": file.filename, "error": "Error converting or transcribing file"}

if __name__ == '__main__':
    app.run(debug=True)
