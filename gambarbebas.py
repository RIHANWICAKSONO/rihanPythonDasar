import turtle

# Inisialisasi jendela tampilan
window = turtle.Screen()
window.title("Gambar Pola Python")
window.bgcolor("white")

# Membuat objek turtle
pen = turtle.Turtle()
pen.speed(1)  # Kecepatan animasi (1 lambat, 10 cepat)
pen.color("blue")
pen.pensize(2)

# Menggambar pola sederhana
for _ in range(36):
    pen.forward(100)
    pen.right(170)

# Menutup jendela saat di-klik
window.exitonclick()