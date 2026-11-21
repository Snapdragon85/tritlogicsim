import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Ternary")
root.configure(background="blue")
root.minsize(200,200)
root.maxsize(500,500)
root.geometry("300x300+50+50")

butn = tk.Button(root, text="Create MOSFET-N")
butp = tk.Button(root, text="Create MOSFET-P")
butn.pack(pady=40)
butp.pack(pady=40)

root.mainloop()