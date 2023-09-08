import tkinter as tk
from tkinter import ttk

# fungsi untuk menghitung hasil
def hitung():
    angka1 = float(angka_entry.get())
    angka2 = float(angka2_entry.get())
    operator = operator_combobox.get()
    
    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        if angka2 == 0:
            hasil = "Error: Pembagian dengan nol"
        else:
            hasil = angka1 / angka2
    else:
        hasil = "Operator Tidak Valid"
    
    hasil_label.config(text=str(hasil))

# membuat jendela
window = tk.Tk()
window.title("KALKULATOR")  # Perbaikan pada title

# frame input
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10)

# entry angka 1
angka_label = ttk.Label(input_frame, text="Angka 1:")
angka_label.grid(row=0, column=0, sticky="w")
angka_entry = ttk.Entry(input_frame)
angka_entry.grid(row=0, column=1)

# entry angka 2
angka2_label = ttk.Label(input_frame, text="Angka 2:")
angka2_label.grid(row=1, column=0, sticky="w")
angka2_entry = ttk.Entry(input_frame)
angka2_entry.grid(row=1, column=1)

# calculator operator
operator_label = ttk.Label(input_frame, text="Operator:")
operator_label.grid(row=2, column=0, sticky="w")
operator_combobox = ttk.Combobox(input_frame, values=("+", "-", "*", "/"))
operator_combobox.grid(row=2, column=1)  # Perbaikan pada baris ini

# tombol hitung
hitung_button = ttk.Button(input_frame, text="Hitung", command=hitung)  # Perbaikan pada text
hitung_button.grid(row=3, columnspan=2, pady=10)  # Perbaikan pada grid

# label hasil
hasil_label = ttk.Label(window, text="")
hasil_label.pack()

window.mainloop()