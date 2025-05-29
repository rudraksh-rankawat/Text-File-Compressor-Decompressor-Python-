import tkinter as tk
from tkinter import filedialog
from utilites import compress, decompress


window = tk.Tk()
window.resizable(False, False)

def open_dialog_for_compress():
    filename = filedialog.askopenfilename(
        title='Open a filee',
        filetypes=(
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
    )
    print(f"File to be compressed: {filename}")
    compress(filename)

def open_dialog_for_decompress():
    filename = filedialog.askopenfilename(
        title='Open a filee',
        filetypes=(
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
    )
    print(f"File to be decompressed: {filename}")
    decompress(filename)

tk.Button(text="Select File to Compress", command=open_dialog_for_compress).pack()
tk.Button(text="Select File to Decompress", command=open_dialog_for_decompress).pack()
window.mainloop()


