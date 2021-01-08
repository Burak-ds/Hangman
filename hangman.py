
import pandas as pd
import random
import sys
from termcolor import colored, cprint
print("********************")
text1 = colored('WELCOME TO HANGMAN', 'blue', attrs=['reverse', 'blink'])
print(text1)
print("********************")




atasozleri = pd.read_csv("/Users/burakgun/Desktop/atasozler.txt")

atasozleri = atasozleri.values.tolist()
random_sayı = random.randint(1,len(atasozleri))
atasozu = atasozleri[random_sayı][0]
atasozu_split = list(atasozu)
tahmin_hakkı = 6

##atasozu sansürlü halde oluşturma

sansurlu = list()
for i in atasozu_split:
    if (i ==" "):
        sansurlu.append("/")
    else:
        sansurlu.append("-")
#Print Kısmını Formatlamaca
#
print_listesi= []
for i in sansurlu:
    if i == "/":
        print(print_listesi)
        print_listesi=[]
    else:
        print_listesi.append(i)
print(print_listesi)
#Print Kısmını Formatlamaca
##Buraya kadar tahmin hakkı var veriler atandı şimdi döngüye geçiyoruz
while tahmin_hakkı>0:
    harf = input("Bir harf tahmin ediniz..")
    if harf in atasozu:
        for k in range(0,len(atasozu)):
            if (atasozu[k]==harf):
                sansurlu[k] = harf
        print_listesi = []
        for i in sansurlu:
            if i == "/":
                print(print_listesi)
                print_listesi = []
            else:
                print_listesi.append(i)
        print(print_listesi)
        print(colored("Kalan Tahmin Hakkı: {}".format(tahmin_hakkı),'red',attrs=['reverse', 'blink']))
    else:
        print("Yanlış Harf")
        tahmin_hakkı -= 1
        print(colored("Kalan Tahmin Hakkı: {}".format(tahmin_hakkı),'red',attrs=['reverse', 'blink']))
if tahmin_hakkı == 0:
    print("Kaybettiniz")
else:
    print("Kazandınız")
print(atasozu)

