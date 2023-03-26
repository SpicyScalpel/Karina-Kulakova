#�������� ��������� ��� �������� ������ �� ����������.

#���������� ������������ ������� ��������� �������.
#��������:
#Tase 1, Tase 2, Tase 3
#���������� ��������(+,-,/,*,**)
#�������� �������� ������������ �����.

#� ��������� ��������� ������� "��������" �������, � ������ ��������� ���������� ������.
#����� ���������� ������������� ������, ����������� ��� �������������.

#��������� ������� ������ �� �����.(����� ������� ������� ���������� ��������)

#� ����� ������ ���������, ���� �������� ������������ ������.
#<60% - Hinne 2
#60-75% - Hinne 3
#75-90% - Hinne 4
#>90% - Hinne 5

from math import *

from random import *
Tase1 = ["+"]
Tase2 = ["+","-"]
Tase3 = ["+","-","/","*"]

try:
    Tasevalimine = int(input("����� ��������� ���������? ����� ����� 1, 2 ��� 3 -> "))
    Katse = int(input("������� �������� ������ ������? ����� ����� -> "))
except ValueError:
    print("����� ������ �����!")
    
oiged_vastused = 0

for i in range(Katse):
    if Tasevalimine == 1:
        n = randint(1,51)
        m = randint(-51,51)
        k = choice(Tase1)
    elif Tasevalimine == 2:
        n = randint(-50,101)
        m = randint(-100,101)
        k = choice(Tase2)
    else:
        n = randint(1,500)
        m = randint(-500,0)
        k = choice(Tase3)

    Kusimus = f"{n} {k} {m}"
    Vastus = input(f"����� ����� �� ������ {Kusimus}: ")
    if str(eval(Kusimus)) == Vastus.strip():
        print("���������!")
        oiged_vastused += 1
    else:
        print(f"�����������! ���������� �����: {eval(Kusimus)}")

if Katse == 0:
    print("�� ������ ���������� �������.")
else:
    protsent = oiged_vastused / Katse * 100
    print(f"�� ������ {oiged_vastused} �� {Katse} ��������. ������: ", end="")
    if protsent < 60:
        print("Hinne 2")
    elif protsent < 75:
        print("Hinne 3")
    elif protsent < 90:
        print("Hinne 4")
    else:
        print("Hinne 5")