import random as r
import os

os.system('clear')
şans = 10
kazan = 0
puan = 0
while True:
 print("+"*71)
 print("\t\t\tTAHMİN OYUNU\n\t\t1-100 ARASI SAYI TAHMİN EDİN!")
 print("Kazanılan:",kazan,"\tPuan:",puan,"\tŞans:",şans)
 print("+"*71)
 rakib = r.randint(1,100)
 try:
  tahEt = int(input("Bir Sayı Tahmin Et: "))
  print("\n\n")
 except ValueError:
    print("\n\n")
    print("="*71)
    print("Rakam Yazman Gerekiyor!")
    print("="*71)
    ent1 = str(input("\n\n+++Ekranı Temizlemek İçin Enter Vur+++"))
    os.system('clear')
    continue
 if tahEt == rakib:
  puan +=5
  kazan +=1
  print("="*71)
  print("Kazandınız!")
  print("="*71)
  print("Tahmin Edilmeli:",rakib)
  print("="*71)
  print("\n")
  ent2 = str(input("+++Ekranı Temizlemek İçin Enter Vur+++"))
  if şans == 10:
      os.system('clear')
      continue
  şans +=1
  os.system('clear')
  continue
 else:
  print("="*71)
  print("Kaybettiniz!")
  print("="*71)
  print("Tahmin Edilmeli:",rakib)
  print("="*71)
  print("\n")
  ent3 = str(input("\n\n+++Ekranı Temizlemek İçin Enter Vur+++"))
  şans -=1
  if şans <= 0:
    print("\n\n")
    print("="*71)
    print("10 Şansınızın Hepsini Kayb Ettiniz!")
    print("="*71)
    print("\n\n")
    break
  if puan <=0:
   os.system('clear')
   continue
  puan -=5
  os.system('clear')
  continue
