print("Tere! Olen sinu uus sõber — Python!")
name=input("Mis on sinu nimi on?")
print("Oi kui ilus nimi!", name)
indeks=input(name + ", Kas leian Sinu keha indeksi? 0-ei, 1-jah=>") #kirjuta pikkus murdarvuna
if indeks=="0":
  print("Kahju! See on väga kasulik info!")
  print()
  print("Kohtimiseni, "+name+"! Igavesti Sinu, Python!")
if indeks=="1":
  try:
      pikkus=float(input("Pikkus: "))
  except:
      pikkus=175
      print("Error, siis pikkus= 175")
  try:
      mass=float(input("Mass: "))
  except:
      mass=55
      print("Error, siis mass= 55")
  indeks=mass/(pikkus)**2
  print(name + ", sinu keha indeks on:", round(indeks,1))
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
    print()
