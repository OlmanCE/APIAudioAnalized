import os
import subprocess

def convert_opus_to_wav(input_file_path, output_file_path, output_file_name):
    try:
        # Construir la ruta completa del archivo de salida
        output_file_path = os.path.join(output_file_path, output_file_name)
        
        # Llamar a FFmpeg desde Python
        subprocess.run(['ffmpeg', '-i', input_file_path, output_file_path], check=True)
        
        print(f"Archivo convertido con éxito y guardado en {output_file_path}")
    except FileNotFoundError:
        print("Error: El archivo OPUS no existe.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Ocurrió un error al convertir el archivo OPUS a WAV. Detalles: {str(e)}")

input_opus = 'C:\\Users\\olman\\OneDrive - Estudiantes ITCR\\Documentos\\TEC 2024\\OP\\textProject\\PTT-20240324-WA0015.opus'
output_dir = 'C:\\Users\\olman\\OneDrive - Estudiantes ITCR\\Documentos\\TEC 2024\\OP\\textProject'
output_file_name = 'output.wav'

convert_opus_to_wav(input_opus, output_dir, output_file_name)