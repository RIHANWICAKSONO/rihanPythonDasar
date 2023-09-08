import tkinter as tk
from tkinter import messagebox

def tambah_siswa():
    nama = entry_nama.get()
    tanggal_lahir = entry_tanggal_lahir.get()
    asal_sekolah = entry_asal_sekolah.get()
    nisn = entry_nisn.get()
    nama_ayah = entry_nama_ayah.get()
    nama_ibu = entry_nama_ibu.get()
    nomor_telepon = entry_nomor_telepon.get()
    alamat = entry_alamat.get()
    
    if not nama:
        messagebox.showerror("Error", "Nama siswa harus diisi")
        return
    
    # Menambahkan data siswa ke daftar
    data_siswa.insert(tk.END, f"{nama}, {tanggal_lahir}, {asal_sekolah}, {nisn}, {nama_ayah}, {nama_ibu}, {nomor_telepon}, {alamat}")
    
    # Mengosongkan input fields
    entry_nama.delete(0, tk.END)
    entry_tanggal_lahir.delete(0, tk.END)
    entry_asal_sekolah.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_nama_ayah.delete(0, tk.END)
    entry_nama_ibu.delete(0, tk.END)
    entry_nomor_telepon.delete(0, tk.END)
    entry_alamat.delete(0, tk.END)

def hapus_siswa():
    selected_item = data_siswa.curselection()
    if selected_item:
        data_siswa.delete(selected_item)

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Data Siswa")

# Membuat label dan input fields untuk data siswa
label_nama = tk.Label(root, text="Nama Siswa:")
entry_nama = tk.Entry(root, width=30)

label_tanggal_lahir = tk.Label(root, text="Tanggal Lahir:")
entry_tanggal_lahir = tk.Entry(root, width=30)

label_asal_sekolah = tk.Label(root, text="Asal Sekolah:")
entry_asal_sekolah = tk.Entry(root, width=30)

label_nisn = tk.Label(root, text="NISN:")
entry_nisn = tk.Entry(root, width=30)

label_nama_ayah = tk.Label(root, text="Nama Ayah:")
entry_nama_ayah = tk.Entry(root, width=30)

label_nama_ibu = tk.Label(root, text="Nama Ibu:")
entry_nama_ibu = tk.Entry(root, width=30)

label_nomor_telepon = tk.Label(root, text="Nomor Telepon:")
entry_nomor_telepon = tk.Entry(root, width=30)

label_alamat = tk.Label(root, text="Alamat:")
entry_alamat = tk.Entry(root, width=30)

# Tombol untuk menambahkan dan menghapus siswa
tambah_button = tk.Button(root, text="Tambah Siswa", command=tambah_siswa, pady=10)
hapus_button = tk.Button(root, text="Hapus Siswa", command=hapus_siswa, pady=10)


# Membuat daftar untuk menampilkan data siswa
data_siswa = tk.Listbox(root, width=70, height=10)

# Menampilkan elemen-elemen di jendela
label_nama.pack()
entry_nama.pack()
label_tanggal_lahir.pack()
entry_tanggal_lahir.pack()
label_asal_sekolah.pack()
entry_asal_sekolah.pack()
label_nisn.pack()
entry_nisn.pack()
label_nama_ayah.pack()
entry_nama_ayah.pack()
label_nama_ibu.pack()
entry_nama_ibu.pack()
label_nomor_telepon.pack()
entry_nomor_telepon.pack()
label_alamat.pack()
entry_alamat.pack()

tambah_button.pack()
hapus_button.pack()
data_siswa.pack()

root.mainloop()