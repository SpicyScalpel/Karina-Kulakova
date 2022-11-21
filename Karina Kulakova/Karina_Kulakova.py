from math import *
#import math math.sqrt()


print("Tere tulemast!!!") #kommenteerime
hinne=int(input("Mis hinne sa said täna?"))
if hinne>=1 and hinne<=5:
	if hinne==1 or hinne==2:
		vastus="Väga halb töö!"
	elif hinne==3:
		vastus="Rahuldav"
	elif hinne==4:
		vastus="Hea"
	else:
		vastus="Väga hea"
else:
	Vastus="Viga andmetega!"
print(vastus)

a=float(input("Kõrgus: ")) #int, float, str, bool
b=float(input("Laius: "))
if a>0 and b>0: # ==,!=,>=,<= or, not                        1 and 1=1
	S=a*b #*,/,+,-,^,//,%,**, d=e=4
else:
	S="ei saa leida"
print("Pindala: ",S)
d=round(sqrt(a**2+b**2),2)
print("d= "+str(d))
text="A"
print(text*5,end='')
print (text)






