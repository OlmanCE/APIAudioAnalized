
# API Transcribir audios
Esta API es un servicio web construido con FastAPI que permite convertir archivos de audio en formato OPUS a WAV y transcribir el contenido de audio a texto, retorna una descripción en formato JSON.
Para ser implementando en el sistema requiere que el sistema tenga instalado.
Las dependencias se encuentran en el archvio requeriments.txt 

| Características

    Conversión de Audio: Convierte archivos de audio de formato OPUS a formato WAV utilizando ffmpeg.
    Transcripción de Voz a Texto: Transcribe audio a texto utilizando la API de Google Speech-to-Text.
    Asíncrono: Toda la lógica de procesamiento se ejecuta de manera asíncrona para optimizar el rendimiento en operaciones I/O intensivas.
    Manejo de Archivos Temporales: Utiliza directorios temporales para manejar los archivos de entrada y salida, garantizando la limpieza de datos después de su procesamiento.
## Authors
- [@FabricioAA223](https://github.com/FabricioAA223)
- [@Olmance ](https://github.com/OlmanCE)


## API Reference

#### Enviar N audios a procesar

```http
  POST /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `audio` | `.OPUS` | puerto/convert-and-transcribe/ |

Toma N cantidad de audios y devuelve la transcripción en formato JSON.
## Deployment

Clona este repositorio.
En el archivo requeriments, se adjuntan las bibliotecas necesarias. 

```bash
  pip install fastapi uvicorn aiofiles python-speechrecognition
```

Ejecuta el servidor usando Uvicorn:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000

```


## Running Tests

Ejemplo de Uso

- Envía una petición POST al servidor usando una herramienta como curl:

```bash
  curl -F "files=@tu_archivo.opus" http://localhost:8000/convert-and-transcribe/
```


## Screenshots

![ Test desde Postman](https://github.com/OlmanCE/APIAudioAnalized/assets/114628295/22675ffb-70d7-4041-afe6-346692393819)
## Documentation

[Install FFMPEG](https://ffmpeg.org/download.html )