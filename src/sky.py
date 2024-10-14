import tkinter as tk
from tkinter import ttk
import pymem as pm
import psutil
import os
import time

processes = []

def getprocess():
    global processes
    processes.clear() 
    for process in psutil.process_iter(['pid', 'name']):
        try:
            processes.append(process.info['name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def app():
    sky = tk.Tk()
    sky.geometry("280x320")
    sky.iconbitmap("logo.ico")
    processlabel = tk.Label(sky, text="Welcome to Sky\nSelect Process:")
    process_option = tk.StringVar()
    process_option.set("Select Process")
    process_selected = ttk.OptionMenu(sky, process_option, *processes)
    
    
    
    processlabel.pack(pady=10)
    process_selected.pack(pady=10)
    sky.mainloop()

if __name__ == "__main__":
    getprocess()
    app()