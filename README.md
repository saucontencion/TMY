transcripcion y mapeo de videos de miducv


# tareas a realizar

1. simplificar 1_whisper_transcription_nemo_diarization.py

2. convertir a pdf lo resultante

3. pasarlo por gpt para que haga mapmark , crear el mapa markmap

4. subirlo como paginas a github 


Instalar las dependencias:
Asegúrate de tener instaladas las librerías necesarias:

bash
Copiar código
pip install yt-dlp faster-whisper reportlab
Ejecutar el script:
Guarda el código en un archivo, por ejemplo, transcribe_youtube_to_pdf.py, y ejecútalo:

bash
Copiar código
python transcribe_youtube_to_pdf.py
Este código descargará el audio del video de YouTube especificado, lo transcribirá utilizando el modelo Whisper, y luego guardará la transcripción en un archivo PDF. El archivo PDF se guardará en el directorio ./downloads con el nombre transcription.pdf.