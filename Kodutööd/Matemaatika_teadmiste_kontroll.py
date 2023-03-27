#Написать программу для проверки знаний по математике.

#Предложить пользователю выбрать сложность заданий.
#Например:
#Tase 1, Tase 2, Tase 3
#количество действий(+,-,/,*,**)
#величину случайно генерируемых чисел.

#В программе случайным образом "задаются" примеры, с учетом сложности провряемых знаний.
#После введенного пользователем ответа, проверяется его правильностью.

#Придумать условие выхода из цикла.(можно сначала указать количество примеров)

#В конце работы программы, надо сообщить тестируемому оценку.
#<60% - Hinne 2
#60-75% - Hinne 3
#75-90% - Hinne 4
#>90% - Hinne 5
#!!!strip() - это метод строки в Python, который удаляет все указанные символы в начале и конце строки (по умолчанию удаляются пробельные символы).
#!!!f перед строкой - это так называемая "f-строка" (или форматированная строка) в Python, которая позволяет вставлять значения переменных и выражений внутри строки.

from math import *

from random import *
Tase1 = ["+"]
Tase2 = ["+","-"]
Tase3 = ["+","-","/","*"]

try:
    Tasevalimine = int(input("Какую сложность выбираешь? Введи число 1, 2 или 3 -> "))
    Katse = int(input("Сколько примеров хочешь решить? Введи число -> "))
except ValueError:
    print("Введи только число!")
    
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
    Vastus = input(f"Введи ответ на пример {Kusimus}: ")
    if str(eval(Kusimus)) == Vastus.strip():      
        print("Правильно!")
        oiged_vastused += 1
    else:
        print(f"Неправильно! Правильный ответ: {eval(Kusimus)}")

if Katse == 0:
    print("Не задано количество заданий.")
else:
    protsent = oiged_vastused / Katse * 100
    print(f"Вы решили {oiged_vastused} из {Katse} примеров. Оценка: ", end="")
    if protsent < 60:
        print("Hinne 2")
    elif protsent < 75:
        print("Hinne 3")
    elif protsent < 90:
        print("Hinne 4")
    else:
        print("Hinne 5")
