import random

# Считываем вопросы и ответы из файла
def read_kusimused_vastused():
    with open('kusimused_vastused.txt', 'r') as file:
        lines = file.readlines()
        kusimused_vastused = {}
        for line in lines:
            kusimus, vastus = line.strip().split(":")
            kusimused_vastused[kusimus] = vastus
    return kusimused_vastused

# Считываем вопросы и ответы из файла в два списка
def read_vastused():
    with open("kusimused_vastused.txt", "r") as fail:
        spisok1=[]
        spisok2=[]
        for line in fail:
            a=line.find(",")
            spisok1.append(line[0:a].strip())
            spisok2.append(int(line[a+1:len(line)].strip()))
    print(spisok1)
    print(spisok2)
    return spisok1, spisok2

# Считываем вопросы и ответы из файла
kusimused_vastused = read_kusimused_vastused()

# Kоличество опрашиваемых
inimeste_arv = 2

# Список принятых и не принятых соискателей
vastuvõetud = []
eisoobi = []

# Опрашиваем каждого соискателя
for i in range(inimeste_arv):
    nimi = input("Palun kirjutage Teie nimi: ")
    print(f'\nTere, {nimi}! Laseme teiega vestluse läbi.')
    random_kusimused = random.sample(list(kusimused_vastused.keys()), 5)
    oiged_vastused = 0
    for kusimused in random_kusimused:
        vastus = input(f"{nimi}, {kusimused}: ")
        if vastus == kusimused_vastused[kusimused]:
            print("Õige!")
            oiged_vastused +=1
        else:
            print(f"Vale! Õige vastus on: {kusimused_vastused[kusimused]}")
    if oiged_vastused >=3:
        print(f"Tore, {nimi}! Teie täitsite küsimustiku edukalt ja tulemused on {oiged_vastused}/5.")
        vastuvõetud.append(nimi, oiged_vastused)
    else: 
        print(f"Kahjuks, {nimi}, Te ei sooritanud meie küsimustiku! Teie õiged vastused on: {oiged_vastused}/5.")
        eisoobi.append(nimi, oiged_vastused)


# Сортируем списки принятых и не принятых соискателей
vastuvõetud.sort(key=lambda x: x[1], reverse=True)
eisoobi.sort()

# Записываем списки принятых и не принятых соискателей в файлы
with open('vastuvõetud.txt', 'w+') as f:
    for nimi, punktid in vastuvõetud:
        f.write(f'{nimi}: {punktid}\n')

with open('eisoobi.txt', 'w+') as f1:
    for nimi in eisoobi:
        f1.write(f'{nimi}: {punktid}\n')

#Выводим списки на экран
print("Принятые соискатели:")
for nimi, punktid in vastuvõetud:
    print(f'{nimi} - {punktid} правильных ответов')

print("\nНе принятые соискатели:")
for nimi, punktid in eisoobi:
    print(f'{nimi} - {punktid} правильных ответов')


