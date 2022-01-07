# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 12:39:28 2022

@author: Manish Kumar Goswami

"""

#importing tkinter, random and string 

from tkinter import *
from tkinter import messagebox, ttk
import random
import string

root = Tk()
root.title("Password Generator MKG") #title of box
root.geometry("450x250")  #box dimension
n = StringVar()
password = StringVar()
data = '@$%#!&_*' + string.ascii_letters + string.digits
len = Label(root, text='Select Length: ', font=('ariel 15 bold'))
len.place(x=60, y=60)
combo = ttk.Combobox(root, width=8, textvariable=n, font=('ariel 15 bold'))
combo['values'] = [i for i in range(8,16)]
combo.place(x=213, y=60)
paswd = Label(root, textvariable=password, font=('ariel 12 bold'), fg='red')
paswd.place(x=80, y=180)

#function for Password Generator
def generate():
    try:
        if n.get()=='':
            messagebox.showinfo("Password Geneartor", "Please select the Length for your Password")
        passw = random.choices(data, k=int(n.get()))
        password.set("Generated Password is: "+''.join(passw))
    except:
        pass
gen = Button(root, text='Generate Your Password', bg='black', fg='green', font=('ariel 15 bold'), relief=GROOVE, command=generate)
gen.place(x=95, y=110)
root.mainloop()