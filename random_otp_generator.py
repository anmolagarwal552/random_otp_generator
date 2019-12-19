from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.geometry('300x100')
root.config(bg='black')
def getotp():
    messagebox.showinfo(title='OTP',message=f'YOUR OTP IS: {random.randint(1000,9999)}')
Label(text='======OTP GENERATOR======',font=10).pack(fill='x',pady=6)
button1 = Button(text='Generate',command=getotp,padx=10).pack(pady=2)
root.mainloop()
