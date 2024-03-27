from typing import List
import os
import subprocess
import tempfile
import speech_recognition as sr
import aiofiles  # Para manejo asíncrono de archivos
import asyncio
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

async def convert_opus_to_wav(input_file_path: str, output_file_path: str) -> str:
    loop = asyncio.get_running_loop()
    try:
        # Usa una función lambda o una función definida para pasar los argumentos correctamente
        await loop.run_in_executor(None, lambda: subprocess.run(['ffmpeg', '-i', input_file_path, output_file_path], check=True))
        return output_file_path
    except Exception as e:
        print(f"Error al convertir el archivo: {str(e)}")
        return ""

async def transcribe_wav_to_text(wav_file_path: str, language: str = "es-ES") -> str:
    loop = asyncio.get_running_loop()
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(wav_file_path) as source:
            audio_data = recognizer.record(source)
        # Ejecuta la transcripción de manera asíncrona en el ThreadPoolExecutor
        text = await loop.run_in_executor(None, lambda: recognizer.recognize_google(audio_data, language=language))
        return text
    except sr.UnknownValueError:
        return "Error: El audio no pudo ser entendido."
    except sr.RequestError as e:
        return f"Error: No se pudo solicitar resultados del servicio de reconocimiento de voz; {e}"

async def process_audio_file(file: UploadFile) -> dict:
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, file.filename)
        output_wav_path = os.path.join(tmpdir, "output.wav")

        # Usar aiofiles para escribir el archivo de manera asíncrona
        async with aiofiles.open(input_path, 'wb') as out_file:
            content = await file.read()  # Leer el contenido del archivo
            await out_file.write(content)

        converted_path = await convert_opus_to_wav(input_path, output_wav_path)
        if converted_path:
            text = await transcribe_wav_to_text(converted_path)
            return {"filename": file.filename, "transcription": text}
        else:
            return {"filename": file.filename, "error": "Error converting or transcribing file"}

@app.post("/convert-and-transcribe/")
async def convert_and_transcribe(files: List[UploadFile] = File(...)):
    results = await asyncio.gather(*(process_audio_file(file) for file in files))
    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
