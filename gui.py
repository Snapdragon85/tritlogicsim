import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Ternary")
root.configure(background="navy")
root.minsize(200,200)
root.attributes('-fullscreen', True)
root.geometry("300x300")

butn = tk.Button(root, text="Create MOSFET-N", width=15, height=2, font=("Arial", 20))
butp = tk.Button(root, text="Create MOSFET-P", width=15, height=2, font=("Arial", 20))
exit = tk.Button(root, text="Exit", command=root.destroy, width=15, height=2, font=("Arial", 20))

butn.grid(row=0, column=0, padx=0, pady=0)
butp.grid(row=0, column=1, padx=0, pady=0)
exit.grid(row=0, column=2, columnspan=2, padx=0, pady=0)

root.mainloop()