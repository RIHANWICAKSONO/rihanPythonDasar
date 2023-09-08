import turtle

def fibonacci_tree(t, branch_len, angle, level):
    if level > 0:
        t.forward(branch_len)
        t.right(angle)
        fibonacci_tree(t, branch_len - 15, angle, level - 1)
        t.left(2 * angle)
        fibonacci_tree(t, branch_len - 15, angle, level - 1)
        t.right(angle)
        t.backward(branch_len)

# Inisialisasi jendela tampilan
window = turtle.Screen()
window.title("Pohon Fibonacci")
window.bgcolor("white")

# Membuat objek turtle
pohon = turtle.Turtle()
pohon.speed(0)  # Kecepatan animasi (0 maksimum)

# Mengatur posisi awal dan sudut awal
pohon.penup()
pohon.goto(0, -250)
pohon.pendown()
pohon.left(90)

# Menggambar pohon Fibonacci
fibonacci_tree(pohon, 150, 20, 7)

# Menutup jendela saat di-klik
window.exitonclick()