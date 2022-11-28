from math import *
j=0
for i in range(0,15,1): #range (15)
	A=float(input(f"{i+1} Sisesta A : ")) #A=5.0 int(A)==A =True
	if int(A)==A:
		j+=1
print(j)

j=0
while True:
	i+=1
	A=float(input(f"{i} Sisesta A : "))
	if int(A)==A: j+=1
	if i==15: break
print(j)

j=0
i=0
while i<15:


