import PySimpleGUI as sg
from datetime import datetime

# Inisialisasi data pelanggan
pelanggan = []

# Fungsi untuk menghitung biaya parkir
def hitung_biaya(jam_masuk, jam_keluar):
    durasi = jam_keluar - jam_masuk
    biaya = durasi.seconds // 60 * 2000  # Menghitung biaya dalam menit
    return biaya

# Membuat tampilan GUI
layout = [
    [sg.Text("Nomor Polisi"), sg.InputText(key="nopol")],
    [sg.Text("Jam Masuk (HH:MM)"), sg.InputText(key="jam_masuk")],
    [sg.Text("Jam Keluar (HH:MM)"), sg.InputText(key="jam_keluar")],
    [sg.Button("Simpan"), sg.Button("Cari NoPol"), sg.Button("Daftar Terakhir"), sg.Button("Daftar Banyak Bayar")],
    [sg.Listbox(values=[], size=(40, 5), key="output")]
]

window = sg.Window("Program Parkir", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Simpan":
        nopol = values["nopol"]
        jam_masuk = datetime.strptime(values["jam_masuk"], "%H:%M")
        jam_keluar = datetime.strptime(values["jam_keluar"], "%H:%M")
        biaya = hitung_biaya(jam_masuk, jam_keluar)
        pelanggan.append((nopol, jam_masuk.strftime("%H:%M"), jam_keluar.strftime("%H:%M"), biaya))
        window["output"].update(pelanggan)

    if event == "Cari NoPol":
        nopol_cari = values["nopol"]
        hasil_cari = [pel for pel in pelanggan if pel[0] == nopol_cari]
        window["output"].update(hasil_cari)

    if event == "Daftar Terakhir":
        if pelanggan:
            terakhir_masuk = pelanggan[-1]
            window["output"].update([terakhir_masuk])

    if event == "Daftar Banyak Bayar":
        if pelanggan:
            pelanggan.sort(key=lambda x: x[3], reverse=True)
            window["output"].update(pelanggan)

window.close()