# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 08:55:59 2023

@author: Excalibur
"""

# 4. hafta notları


import tkinter as tk
from tkinter import messagebox

def metni_bicimlendir():
    etiket["text"] = "Teknik Bilimler"
    messagebox.showerror(title="HATA!", message="HATA VAR")
    messagebox.showinfo(title="BİLGİLENDİR", message="bilgilendirme")
    messagebox.showwarning(title="dikkat", message="önemli uyarı")

def router2():
    pencere2.deiconify() # gizlenen pencereyi aktif etme

pencere = tk.Tk()
pencere2 = tk.Toplevel()  # alt pencere
pencere2.withdraw()  # pencere gizleme

routerLabel = pencere2

pencere.title('Pencere başlık!')
pencere2.title("Pencere2")
pencere.geometry('300x500')
pencere2.geometry("800x500")

etiket = tk.Label(text='Kullanıcı Adı: ',
                  fg='BLUE',
                  font='Times 30 bold italic')

etiket2 = tk.Label(text='Şifre: ',
                   fg='BLACK',
                   font='Times 30 bold italic')

dugme = tk.Button(text='Giriş Yap',
                  command=router2,
                  activebackground="pink",
                  activeforeground="pink",
                  font="times 30 italic")

pencere2label = tk.Label(routerLabel,text='Anasayfa: ',
                   fg='RED',
                   font='Times 30 bold italic')

etiket.pack()
etiket2.pack()
dugme.pack()
pencere2label.pack()
pencere.mainloop()

## ornek 1
"""
pencere=tkinter.Tk()
pencere.title('Hata!')
pencere.geometry('500x600')

etiket= tkinter.Label(text='Hitit Üniversitesi',
                    fg ='BLUE',
                    bg ='#00AAcc',
                    font ='Times 30 bold italic',
                    )
def metni_bicimlendir():
    etiket["text"]="Teknik Bilimler"
    messagebox.showerror(title="HATA!", message="HATA VAR")
    messagebox.showinfo(title="BİLGİLENDİR", message="bilgilendirme")
    messagebox.showwarning(title="dikkat", message="önemli uyarı")
    
dugme=tkinter.Button(text='tamam',
                     command=metni_bicimlendir,
                     activebackground ="pink",
                     activeforeground ="pink",
                     font="times 30 italic")
                     
                     

etiket.pack()
dugme.pack()
pencere.mainloop()"""
