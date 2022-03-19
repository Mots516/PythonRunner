from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk


def AfterLog():
    result = tk.Tk()
    result.geometry('500x500')
    result.title('Thank You !')

    # Background Colors
    result.configure()

    # Locking the window size
    result.resizable(width=False, height=False)

    # Showing Result
    label = tk.Label(result, text = 'Thank You For Using Our System !!!!',font=('Arial',12, 'bold'),bg='white', fg='green').place(relx = 0.5, rely = 0.5, anchor = CENTER)


AfterLog()
