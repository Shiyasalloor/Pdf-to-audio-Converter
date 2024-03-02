import PyPDF2
from gtts import gTTS
import os

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_voice(text, language='en'):
    tts = gTTS(text = text, lang = language, slow = False)
    return tts

def save_voice(tts,output_path):
    tts.save(output_path)

pdf_path = './ER Model.pdf'
text = pdf_to_text(pdf_path)
tts = text_to_voice(text)
output_path = './output2.mp3'
save_voice(tts, output_path)
os.system('start ' + output_path)


