print("Tere! Olen sinu uus sõber — Python!")
name=input("Mis on sinu nimi on?")
print("Oi kui ilus nimi!", name)
indeks=input(name + "Kas leian Sinu keha indeksi? 0-ei, 1-jah=>")
if indeks=="1":

      while True:

          try:
              pikkus=int(input("Pikkus: "))
              if pikkus>0 and pikkus<273: break
          except:
              print("Error")
      mass=-1
      while mass<0 or mass>400:
          try:
              mass=int(input("Mass: "))
          except:
              print("Error")
            
      try:       
          indeks=mass/pikkus
          print(name + "Sinu keha indeks on:", round(indeks,1))
          if indeks<16:
            print("Tervisele ohtlik alakaal") 
          elif indeks>=16 and indeks<19:
            print("Alakaal")
          elif indeks>=19 and indeks<25:
            print("Normaalkaal")
          elif indeks>=25 and indeks<30:
            print("Ülekaal")
          elif indeks>=30 and indeks<35:
            print("Rasvimune")
          elif indeks>=35 and indeks<40:
            print("Tugev rasvamine")
          elif indeks>=40:
            print("Tervisele ohtlik rasvamine")
          else:
            print("Kahju! See on väga kasulik info!")
