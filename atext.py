import PyPDF2

def extract_text_from_pdf(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
    
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

# Ruta del PDF de transcripción
pdf_path = './downloads/transcription.pdf'

# Ruta donde se guardará el documento de texto
txt_path = './downloads/transcription.txt'

# Extraer texto del PDF y guardarlo en un archivo de texto
extract_text_from_pdf(pdf_path, txt_path)

print("Texto extraído y guardado en:", txt_path)
