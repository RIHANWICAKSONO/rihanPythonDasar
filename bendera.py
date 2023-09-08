import turtle

# Inisialisasi jendela tampilan
window = turtle.Screen()
window.title("Bendera Indonesia")
window.bgcolor("white")

# Membuat objek turtle
bendera = turtle.Turtle()
bendera.speed(0)

# Menggambar warna dasar bendera merah putih
bendera.color("red")
bendera.begin_fill()
bendera.forward(300)
bendera.left(90)
bendera.forward(200)
bendera.left(90)
bendera.forward(300)
bendera.left(90)
bendera.forward(200)
bendera.end_fill()

# Menggambar garis putih di tengah bendera
bendera.penup()
bendera.goto(-150, 0)
bendera.pendown()
bendera.color("white")
bendera.pensize(20)
bendera.forward(300)

# Menutup jendela saat di-klik
window.exitonclick()