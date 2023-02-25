import random
""" 
1- 100 arasinda rastgele uretilecek bir sayiyi asagi yukari ifadeleri ile buldurmaya calsiin. 
*** 100 uzerinden puanlama yapin. Her soru 20 puan 
Hak bilgisi 5 olucak. 
"""
x = random.randint(1, 100)
hakBilgisi = 5 
oyunaDevam = True
print(f"Uretilen rastgele sayi 1-100 arasindadir. Basarilar !!! {x}")
puan = 100 
sayac = 0 
while oyunaDevam : 
    oyuncuCevap = int(input("Lutfen tahmin ettiginiz sayiyi giriniz : "))
    if(oyuncuCevap == x ): 
        print(f"Tahmininiz dogru . Uretilen rastgele sayi : {x}")
        break   
    elif(oyuncuCevap > x ): 
        print("Tahmininiz Dusurunuz!!!")
        hakBilgisi -= 1
        sayac += 1 
        if(hakBilgisi == 0):
            print(f"Hakkiniz bitmistir. Sayi : {x}")
            break
    elif(oyuncuCevap < x ): 
        print("Tahmininiz Arttiriniz !!!")
        hakBilgisi -= 1
        sayac += 1 
        if(hakBilgisi == 0):
            print(f"Hakkiniz bitmistir. Sayi : {x}")
            break

if(sayac == 0) : 
    print(f"Puaniniz : 100")
elif(sayac == 1 ):
    print(f"Puaniniz : 80")
elif(sayac == 2): 
    print(f"Puaniniz : 60")
elif(sayac == 3): 
    print(f"Puaniniz : 40")
elif(sayac == 4): 
    print(f"Puaniniz : 20")
elif(sayac == 5): 
    print(f"Puaniniz : 0 ")
