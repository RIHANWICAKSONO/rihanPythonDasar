#persegi
sisi =  int(input("masukan keliling luas persegi : "))
keliling = sisi + sisi + sisi + sisi
luas = sisi*sisi

print(f"keliling persegi : {keliling}  ")
print(f"luas persegi  : {luas}   ")

#persegi panjang
panjang = int(input("masukan keliling luas persegi panjang : "))
lebar = int(input("masukan lebar panjang : "))
keliling = panjang + lebar
luas = panjang * lebar

print(f"keliling persegi panjang : {keliling} ")
print(f"luas persegi panjang : {luas}")

#trapesium
def hitung_trapesium(alas_atas, alas_bawah, tinggi, sisi_miring):
    luas = 0.5 * (alas_atas + alas_bawah) * tinggi
    keliling = alas_atas + alas_bawah + (2 * sisi_miring)
    return luas,keliling