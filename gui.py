import tkinter as tk
from tkinter import filedialog
import PyPDF2
import pyttsx3
from threading import Thread

class PDFReaderApp:
    def __init__(self, master):
        self.master = master
        master.title("PDF Reader")

        # Layout
        self.play_button = tk.Button(master, text="Play", command=self.play_audio)
        self.play_button.pack()

        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.volume_scale = tk.Scale(master, from_=0.0, to=1.0, resolution=0.1, orient='horizontal', label="Volume")
        self.volume_scale.set(1.0)  # Default volume
        self.volume_scale.pack()

        self.rate_scale = tk.Scale(master, from_=100, to=200, resolution=10, orient='horizontal', label="Speech Rate")
        self.rate_scale.set(150)  # Default rate
        self.rate_scale.pack()

        self.open_file_button = tk.Button(master, text="Open PDF", command=self.open_pdf)
        self.open_file_button.pack()

        self.file_path = ""
        self.text = ""

    def open_pdf(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.file_path:
            self.text = self.read_pdf(self.file_path)

    def read_pdf(self, pdf_path):
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text() + ' '
        return text

    def speak_text(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', self.rate_scale.get())
        engine.setProperty('volume', self.volume_scale.get())
        engine.say(text)
        engine.runAndWait()

    def play_audio(self):
        if self.text:
            # Run the speech in a separate thread to prevent GUI freezing
            Thread(target=self.speak_text, args=(self.text,)).start()
        else:
            tk.messagebox.showinfo("Error", "Please open a PDF file first.")

if __name__ == "__main__":
    root = tk.Tk()
    my_gui = PDFReaderApp(root)
    root.mainloop()
