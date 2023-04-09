import tkinter as tk
from tkinter import filedialog
from docx2pdf import convert

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
print(file_path)
convert(file_path)
