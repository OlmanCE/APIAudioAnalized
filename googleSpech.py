import speech_recognition as sr

# Crea una instancia del reconocedor
r = sr.Recognizer()

# Carga el archivo de audio WAV
with sr.AudioFile('C:\\Users\\olman\\OneDrive - Estudiantes ITCR\\Documentos\\TEC 2024\\OP\\textProject\\output.wav') as source:
    # Escucha el contenido del archivo
    audio_data = r.record(source)
    
    # Intenta reconocer el audio usando Google's speech recognition
    try:
        text = r.recognize_google(audio_data, language='es-ES') 
        print("Transcripción: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition no pudo entender el audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
