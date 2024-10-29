import tkinter as tk
from tkinter import filedialog
from docx2pdf import convert

def convertir_a_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("Word Files", "*.docx")])
    
    if file_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        convert(file_path, output_path)
        status_label.config(text="Conversión finalizada con éxito!")

root = tk.Tk()
root.title("Convertidor Word a PDF")

convert_button = tk.Button(root, text="Convertir a PDF", command=convertir_a_pdf)
convert_button.pack(pady=28)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
