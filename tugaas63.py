import tkinter as tk
from tkinter import ttk
def hitung():
    jumlah_Harga = float(entry_harga.get())
    jumlah_barang = int(entry_barang.get())
    total = jumlah_Harga * jumlah_barang
    
window = tk.Tk()
window.title("Program Kasir")

label_harga = tk.Label(window, text="Harga ")
label_harga.pack()
entry_harga = tk.Entry(window)
entry_harga.pack()

label_barang = tk.Label(window, text="kuantitas ")
label_barang.pack()
entry_barang = tk.Entry(window)
entry_barang.pack()

hitung_button = ttk.Button(window, text="Hitung Total", command=hitung)
hitung_button.pack()

hasil_label = ttk.Label(window, text="")
hasil_label.pack()

window.mainloop()

    