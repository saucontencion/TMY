# ---- libraries ---- #
import os
import yt_dlp
from faster_whisper import WhisperModel
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# ---- download audio from YouTube ---- #
def download_audio(youtube_url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s')
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

# ---- transcribe audio using Whisper ---- #
def transcribe_audio(audio_path):
    model = WhisperModel("base")
    segments, info = model.transcribe(audio_path)
    return segments

# ---- save transcription to PDF ---- #
def save_transcription_to_pdf(transcription, output_pdf_path):
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    width, height = letter

    text = c.beginText(40, height - 40)
    text.setFont("Helvetica", 12)

    for segment in transcription:
        text.textLine(f"[{segment.start:.2f} - {segment.end:.2f}] {segment.text}")

    c.drawText(text)
    c.save()

# ---- main function ---- #
def main():
    youtube_url = "https://www.youtube.com/watch?v=ahiDCefIt60"
    output_path = "./downloads"
    os.makedirs(output_path, exist_ok=True)
    
    # Download audio
    download_audio(youtube_url, output_path)
    
    # Find the downloaded file
    audio_file = None
    for file in os.listdir(output_path):
        if file.endswith(".mp3"):
            audio_file = os.path.join(output_path, file)
            break

    if audio_file:
        # Transcribe audio
        transcription = transcribe_audio(audio_file)

        # Save transcription to PDF
        output_pdf_path = os.path.join(output_path, "transcription.pdf")
        save_transcription_to_pdf(transcription, output_pdf_path)
        print(f"Transcription saved to {output_pdf_path}")
    else:
        print("No audio file found.")

if __name__ == "__main__":
    main()
