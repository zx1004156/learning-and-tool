import tkinter as tk
from tkinter import filedialog

root = tk.Tk()#建立視窗物件
root.withdraw()#隱藏視窗

file_path = filedialog.askopenfilename(parent=root)

if not file_path:
    print('file path is empty')

else:
    print(type(file_path))
