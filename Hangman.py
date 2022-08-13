#### HANGMAN GAME ####
import random as rand

# Rastgele kelimele listesi

ornek_kelime_listesi = ["araba", "armut", "elma", "patates", "elbise", "telefon", "kelime", "kalem", "zeytin", "bilgisayar","binmek", "güvenlik",
"hukuk" ,"kılmak", "modern","okur", "silah", "talep", "yıldız", "yoğun", "asker", "basit", "denilmek", "uygulama","üretilmek", "bayan", "besin",
"görüşmek","yaklaşık","alışveriş","bilinç","çerçeve","lazım","bilgisayar","armut","zeytin","saat","kalem","cüzdan","kulaklık","şişe","perde",
"kütüphane","engin", "konsol","kağıt","klima"]
soru_kelimesi = ornek_kelime_listesi[rand.randint(0,47)]


#### Oyun Listeleri

adam_asma_listesi = [
    "    ______",
    "    |     ",
    "    0     ",
    "  / | \   ",
    " /  |  \  ",
    "    |     ",
    "   / \    ",
    "  /   \   ",
    "          ",
                       ]

current_listesi = []
soru_kelimesi_listesi = []


def soru_kelimesini_liste_yapan_f(a):
    for i in a:
        soru_kelimesi_listesi.append(i)


def baslangıc_durum_listesi_olusturma_f(x):   # Soru kelimesi olacak
    for i in range(len(x)):
        current_listesi.append("-")


def durum_listesini_string_yapan_f(y):
    print("kelimeniz;")
    for i in range(len(y)):
        print(y[i],end ="")
    print(" ")


hata_sayısı = 0
def adam_asma_f():
    adam_asma_listesi
    for i in range(hata_sayısı):
        print(adam_asma_listesi[i])


def hata_sayacı(x):
    global hata_sayısı
    if not x in soru_kelimesi:
        hata_sayısı = hata_sayısı + 1


def harf_alma_fonksiyonu(x, liste):   #liste current list olmalı
    for i in range(len(soru_kelimesi)):
        if  soru_kelimesi[i] == x:
            liste[i] = x

########################################################################################################################

baslangıc_durum_listesi_olusturma_f(soru_kelimesi)
input_sayısı = 0
soru_kelimesini_liste_yapan_f(soru_kelimesi)

while not soru_kelimesi_listesi == current_listesi:

    durum_listesini_string_yapan_f(current_listesi)
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    x = str(input("lütfen_harf_girin"))
    harf_alma_fonksiyonu(x, current_listesi)
    hata_sayacı(x)
    if hata_sayısı ==  9:
        print("Oyun bitti, Zortladın")
        print("Kesbiş olsun")
        print(f'{soru_kelimesi,"was the right answer"}')
        break

    if soru_kelimesi_listesi == current_listesi:
        print("Tebrikler kazandınız")
        print(f'{soru_kelimesi,"was the right answer"}')

    print("Esirin durumu")
    adam_asma_f()
































