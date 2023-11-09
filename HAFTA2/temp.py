
import tkinter as tk # kütüphanae dahil etme

pencere = tk.Tk() # taşıyıcıya aktarma
pencere2 = tk.Tk()

routerlabel = pencere2

pencere.title("Bu bir pencere başlığı") # pencere başlığı
pencere2.title("İkinci Pencere")
pencere.geometry("800x500") # pencere boyutlandırma
pencere2.geometry("500x800")
etkiket = tk.Label(text="Bİrinci Ekran")
etkiket2 = tk.Label(routerlabel,text="2. pneceres",)
etkiket.pack()
etkiket2.pack()



pencere.mainloop() # ekranda döndürme
pencere2.mainloop() # ekranda döndürme






# range

# for

for i in range(2,20,1):
    print(i)
    if(i == 5):
        print("Sayi {0}".format(i))
        break
    

for i in range(10):
    if(i%2 == 0):
        pass
    else:10
        print(i)
    break


# function



def topla(sayi1,sayi2):
    toplama = sayi1+sayi2
    print(toplama)


inputSayi1 = input("ilk sayı gir: ")
inputSayi2 = input("İkinci Sayı gir: ")

topla(float(inputSayi1), float(inputSayi2))


def carpma(sayi1,sayi2):
    sonuc = sayi1 * sayi2
    return sonuc

value = carpma(3,4)

print(value)




        
# while


i = 0
while (i< 30):
    print(i)
    if(i == 5):
        print("Sayi {0}".format(i))
        break
    i+=1



ASAL SAYI BULMA

sayac = 0;
girilenSayi = input("Sayı giriniz")
for i in range(2, int(girilenSayi)):
      if(int(girilenSayi) & i == 0):
          sayac += 1
          break
if(sayac != 0) :
      print("Girilen Sayı Asal DEĞİL")
else:
    print("Sayı Asal")




# prosedür dışarıya değer verir

# degeri içerde tutrar













def asalBulme(girilenSayi):
    sayac = 0;
    girilenSayi;
    for i in range(2, int(girilenSayi)):
          if(int(girilenSayi) & i == 0):
              sayac += 1
              break
    if(sayac != 0) :
          print("Girilen Sayı Asal DEĞİL")
    else:
        print("Sayı Asal")



girilenSayi = input("Sayı gir: ")

asalBulme(girilenSayi)



















# tam sayi için = int(sayi1)
# küsüratlı sayi için = float(sayi1)

# -*- coding: utf-8 -*-

Spyder Editor

This is a temporary script file.
"""


#sdsad

"""
ghj
"""

"""
##
a = 13123;
b = 21;
##
sonuc = a+b ;
print(sonuc);

ay = 12;
kilometre = 3000.0;
sehir = "Isparta";

##
print(ay);
print(kilometre);
print(sehir);

a = 5;
ay = "Ekim";

print(len(ay));

##
print(sehir,kilometre)

##
sayi1 = 200;
sayi2 = 50;
if sayi1 > sayi2 : print("sayi1 sayi2 den büyüktür");

#####3
if sayi1 >= 0 :
    print("sayı sıfır ya da pozitif")
else:
    print("Sayi negatif");
    
    ####3
    if sayi1 > 0 :
        print("Sayı Pozifit")
    elif sayi1 == 0:
        print("sayi sfır")
    else:
        print("Sayı negatif")
        
        
        #####
        
kullaniciadi = 'admin';
sifre = '1234';
if(kullaniciadi=='admin' and sifre=='1234'):
    print("Hoş geldin")
else:
    print("Hata")
    
    #####

sayi = int(input('bir sayı gir:'))
if sayi > 0:
    print('Girdiğiniz sayi pozitif')
elif sayi == 0:
    print('Girdiğiniz sayi sıfırdır')
else:
    print('Girdiğiniz sayı negatif tam sayıdır') """
    
    