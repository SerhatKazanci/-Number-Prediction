import random
import time


def Tahmin():
    while True:
        print("Sayı Tahmin Oyununa Hoş Geldiniz.. \n 1-50 Arasında Bir Sayı Tahmin Ediniz.")
        sayi = random.randint(1, 50)
        tahmin_hakki = 5

        if sayi % 2 == 0:
            print("İpucu : Sayı Çift")
        else:
            print("İpucu : Sayı Tek")

        print("Oyun Kısa Süre İçinde Başlayacaktır.Bekleyiniz..")
        time.sleep(1.5)
        print("3")
        time.sleep(1.5)
        print("2")
        time.sleep(1.5)
        print("1")

        while True:
            tahmin = int(input("Tahmininiz: "))
            tahmin_hakki -= 1

            if tahmin == sayi:
                print("Sayı sorgulanıyor... ")
                time.sleep(1.5)
                print("Tebrikler! doğru bildiniz.Oyun Birazdan Tekrardan Başlayacaktır")
                time.sleep(3)
                break

            elif tahmin_hakki == 0:
                print("Tahmin hakkınız bitmiştir")
                print("Bilgisayarın tahmini: ", sayi)
                print("Yeni Oyun Birazdan Başlaycaktır. Bekleyiniz..")
                time.sleep(3)
                break

            elif tahmin > sayi:
                print("Sayı sorgulanıyor... ")
                time.sleep(1.5)
                print("Daha küçük bir sayı giriniz")
                print("Kalan tahmin hakkı: ", tahmin_hakki)

            else:
                print("Sayı sorgulanıyor... ")
                time.sleep(1.5)
                print("Daha büyük bir sayı giriniz")
                print("Kalan tahmin hakkı: ", tahmin_hakki)


Tahmin()
