import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
root.geometry('300x200')
root.resizable(width=False, height=False)

color1 = '#0a0b0c'
color2 = '#f5267b'
color3 = '#ff3d8d'
color4 = 'BLACK'

main_frame = tk.Frame(root, bg=color1, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)
main_frame.columnconfigure(0, weight=1)



