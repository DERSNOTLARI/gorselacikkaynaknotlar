# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 16:57:51 2023

@author: Excalibur
"""

# 3. HAFTA NOTLARI

def textStyleClass(text,textcolor,backcolor,font):
    etiket["text"] = text
    etiket["fg"] = textcolor
    etiket["bg"] = backcolor
    etiket['font'] = font

import tkinter as tkview


pencere = tkview.Tk()
pencere.geometry("800x500") # ekran boyutlandırma
pencere.title("Hata") # 
etiket = tkview.Label() # label oluşturma



etiket["text"] = "Metin Belirle"
etiket["fg"] = "red"
etiket["bg"] = "black"
etiket['font'] = "Verdana 14 italic"




button = tkview.Button(text="Tamam", command =lambda: 
                       textStyleClass(
                           "Metin Girin",
                           "blue",
                           "#34495e",
                           "Times 60 bold italic"
                           )
                       ) # buton

button.pack() # başlatma
etiket.pack() # başlatma
pencere.mainloop() # ekran açma