# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 08:54:19 2023

@author: Excalibur
"""

usdKuru =  28
euroKuru = 30

def kurHesapla():
    deger = float(e_miktar_giris.get())
    secili_kur = cmb_kursec.get()
    
    if secili_kur == "USD":
        sonuc = deger / usdKuru
    elif secili_kur == "EURO":
        sonuc = deger / euroKuru
    else:
        sonuc = "Geçersiz Kur"
        
    lbl_sonucnokta.config(text=str(sonuc)+"₺")
    
def inputTemizle():
    e_miktar_giris.delete(0, END)
    lbl_sonucnokta.config(text=".....")

from tkinter import * 
from tkinter import ttk


    
anaform = Tk()

anaform.title("Kur Hesapla")
anaform.geometry("400x600")

lbl_tlmiktar = Label(anaform, text="TL(₺) Miktarı Yazın: *")
e_miktar_giris = ttk.Entry(anaform)

lbl_kurturu = Label(anaform, text="Kur Türü Seçin: *")
cmb_kursec = ttk.Combobox(anaform, values=['USD', 'EURO'])


lbl_sonuc = Label(anaform, text="Sonuç")
lbl_sonucnokta = Label(anaform, text="....")

btn_1 = Button(anaform, text="Temizle", command=inputTemizle)
btn_hesapla = ttk.Button(anaform, text="Hesapla", command=kurHesapla)


lbl_tlmiktar.grid(row=0, column=0)
e_miktar_giris.grid(row=0,column=1,pady=5)
lbl_kurturu.grid(row=1,column=0)
cmb_kursec.grid(row=1,column=1,pady=5)

lbl_sonuc.grid(row=2, column=0,pady=5)
lbl_sonucnokta.grid(row=2,column=1)

btn_1.grid(row=3,column=0,pady=5,padx=5),
btn_hesapla.grid(row=3,column=1,pady=5,padx=5)


anaform.mainloop()


"""

lbl_tlmiktar.pack()
cmb_kursec.pack()
btn_1.pack(),
btn_hesapla.pack()

lbl_tlmiktar.pack(expand=NO, fill=BOTH)
cmb_kursec.pack(expand=NO,fill=BOTH, padx=30, pady=40)
btn_1.pack(expand=NO, fill= X,padx=30,pady=40),
btn_hesapla.pack(expand=NO,side= BOTTOM,padx=30,pady=40)
anaform.mainloop()

"""