import tkinter as tk
root = tk.Tk()
Label = tk.Label(root, text="Label 1")
Label.pack()

button = tk.Button(root, text="Tombol 1")
button.pack()

checkbox = tk.Checkbutton(root, text="Centang 1")
checkbox.pack()
root.mainloop()