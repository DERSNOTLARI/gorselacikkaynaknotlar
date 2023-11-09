# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:35:38 2023

@author: Excalibur
"""


def alertDialog(txt_username):
   # messagebox.showinfo(title="Hoşgeldin", message=txt_username.get())
   cevap = messagebox.askyesnocancel(
       title="Hoşgledin",                   
       message=txt_username.get(),
     )
   if cevap is True:
      print("Tamam")
      ana_form.destroy() # alert kapatma
   elif cevap is False:
      print("Hayıra Tıklandı")
   elif cevap is None:
      print("İptal Tıklandı")

      
      
import tkinter as tk
from tkinter import messagebox

ana_form = tk.Tk()

ana_form.title("Giriş Yap")

ana_form.geometry("300x400")


# label
usernamelabel = tk.Label(text="Kullanıcı Adı *")
passwordlabel = tk.Label(text="Şifre *")

# inputlar
txt_username = tk.Entry(ana_form, width=100)
txt_password = tk.Entry(ana_form, width=100)



# buton
login = tk.Button(ana_form, text="Giriş yap",command=lambda:alertDialog(txt_username))

usernamelabel.pack()
txt_username.pack()
passwordlabel.pack()
txt_password.pack()
login.pack()

ana_form.mainloop()
