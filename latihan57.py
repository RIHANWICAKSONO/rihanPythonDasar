import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False, False)
window.title("Sapa")

# Variable
Nama_Depan = tk.StringVar()
Nama_Belakang = tk.StringVar()

# fungsi 1
def tombol_click():
    pesan = f"Hello {Nama_Depan.get()} {Nama_Belakang.get()}, Have a nice day"
    showinfo(title="Hi", message=pesan)

# frame input
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, fill="x", expand=True)

# komponen
# 1. Label nama depan
nama_Depan_label = tk.Label(input_frame, text="Nama Depan: ")
nama_Depan_label.pack(padx=10, fill="x", expand=True)

# 2. entry nama depan
nama_Depan_entry = ttk.Entry(input_frame, textvariable=Nama_Depan)
nama_Depan_entry.pack(padx=10, fill="x", expand=True)

# 3. Label nama belakang
nama_Belakang_label = tk.Label(input_frame, text="Nama Belakang: ")
nama_Belakang_label.pack(padx=10, fill="x", expand=True)

# 4. entry nama belakang
nama_Belakang_entry = ttk.Entry(input_frame, textvariable=Nama_Belakang)
nama_Belakang_entry.pack(padx=10, fill="x", expand=True)

# 5. tombol
tombol = ttk.Button(input_frame, text="Sapa", command=tombol_click)
tombol.pack(fill='x', expand=True, padx=10, pady=10)

window.mainloop()