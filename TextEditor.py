import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        text = file.read()
        text_area.insert('end', text)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    with open(file_path, 'w') as file:
        text = text_area.get('1.0', 'end-1c')
        file.write(text)

root = tk.Tk()
root.title('Text Editor')

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)
menu_bar.add_cascade(label='File', menu=file_menu)

root.config(menu=menu_bar)

text_area = tk.Text(root)
text_area.pack(expand=True, fill='both')

root.mainloop()
