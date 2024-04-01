import PyPDF2
import pyttsx3

def read_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + ' '
    return text

def speak_text(text, rate=150, volume=1.0):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)  # Adjust the speed: default is 200
    engine.setProperty('volume', volume)  # Adjust the volume: 0.0 to 1.0
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    pdf_path = input("Enter the full path to the PDF file: ")
    text = read_pdf(pdf_path)

    rate = input("Enter speech rate (default 150): ")
    rate = int(rate) if rate.isdigit() else 150

    volume = input("Enter volume (0.0 to 1.0, default 1.0): ")
    volume = float(volume) if volume.replace('.', '', 1).isdigit() else 1.0

    speak_text(text, rate, volume)
