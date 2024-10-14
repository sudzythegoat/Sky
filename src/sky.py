import tkinter as tk
import pymem as pm
import os
import time

def app():
    sky = tk.Tk()
    sky.geometry("280x320")
    sky.iconbitmap("logo.ico")
    processlabel = tk.Label(sky, text="Welcome to Sky\nSelect Process:")
    
    processlabel.pack(pady=10)
    sky.mainloop()

if __name__ == "__main__":
    app():