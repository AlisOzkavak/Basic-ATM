print("""
******************************

ATM Programına Hoşgeldiniz :)

İşemler:

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

(Programdan Çıkmak İçin "Q" Tuşuna Basın)

******************************
""")


bakiye = 100

while True:
    işlem = input("İşlem Seçiniz:")

    if (işlem == 'q','Q'):
        print("*****Yine Bekleriz*****")
        break
    elif (işlem == "1"):
        print("Bakiyeniz ${}'dir".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Miktarı Giriniz:"))
        bakiye += miktar
        print("Bakiyeniz:$" , bakiye)        

    elif (işlem == "3"):    
        miktar = int(input("Miktarı Giriniz:"))
        
        if (bakiye - miktar < 0):
            print("İşleminiz Başarısız Oldu")
            print("Bakiyeniz:$", bakiye)
            
            continue
        bakiye -= miktar
        print("İşleminiz Başarıyla Gerçekleşti")
        print("Kalan Bakiyeniz:$", bakiye)

    else:
        print("Geçersiz")

















