#Напишите функцию inimesed(), при запуске которой происходит заполнение двух списков: люди[], рост[]. 
#Количество элементов в списках ограничивается пользователем (либо оговаривается сколько людей надо опросить, либо в режиме online- данные вносятся пока не закончатся данные о людях).
#После заполнения массивов появляется меню с выбором действий:
#• Свой вариант;
#• Отобразить в алфавитном порядке список людей и их рост;
#• Найти самого высокого и самого низкого из людей;
#• Найти средний рост n людей в списке, имена людей вводит пользователь ;
#• Удалить из списка человека и данные о его росте, введя имя человека
#Для описания действий создайте необходимые функции.

# Создаем пустые списки для хранения имен и роста
inimesed = []
pikkused = []

# Запускаем цикл для ввода данных о людях
while True:
    # Вводим имя человека
    inimene = input('Введите имя человека. ')
    # Вводим рост человека
    pikkus = int(input('Введите рост этого человека. '))
    # Добавляем имя и рост в соответствующие списки
    inimesed.append(inimene)
    pikkused.append(pikkus)
    # Проверяем, хочет ли пользователь закончить ввод данных
    log_out = input('Введите "z" для завершения ввода данных о людях \
или Enter для продолжения. ')
    if log_out.lower() == 'z':
        break
print("Cписок людей:")
print(inimesed)

# Создаем словарь, где ключи - имена, а значения - рост
inimene_dict = dict(zip(inimesed, pikkused))

# Функция для получения роста человека по имени
def get_pikkused(inimene, inimesed):
    if inimene in inimesed.keys():
        return f'Рост {inimene} равен {inimesed[inimene]} см.'
    else:
        return 'Такого человека нет в списке.' 

# Функция для вывода информации о людях в алфавитном порядке по имени
def show_inf(inimesed):
    sorted_tuple = sorted(inimesed.items())
    return sorted_tuple

# Функция для поиска самого высокого и самого низкого человека в списке
def koige_pikk_ja_koige_madal(inimesed):
    pikk_max = 0
    isik_max = ''
    pikk_min = float('inf')
    isik_min = ''
    for inimene, p in inimesed.items():
        if p > pikk_max:
            pikk_max = p
            isik_max = inimene
        if p < pikk_min:
            pikk_min = p
            isik_min = inimene
    return f'Самый высокий человек: {isik_max} ({pikk_max} см), самый низкий человек: {isik_min} ({pikk_min} см)'

# Функция для вычисления среднего роста людей
def keskmine_pikkus(inimesed):
    # Получим количество людей для расчета
    n = int(input("Введите количество людей: "))
    
    pikkused = [] # Список ростов людей
    
    for i in range(n):
        nimi = input(f"Введите имя {i+1}-го человека: ")
        pikkus = inimesed[nimi]
        pikkused.append(pikkus)
    
    # Найдем средний рост
    sum_pikkused = sum(pikkused)
    kesk_pikkus = sum_pikkused / n
    
    return f'Средний рост людей: {kesk_pikkus:.2f} см.'

 
def delete_person(inimesed):
    inimene = input("Введите имя человека для удаления: ")
    if inimene in inimesed:
        del inimesed[inimene]
        print(f"{inimene} удален(а) из списка")
    else:
        print(f"{inimene} не найден(а) в списке")

    print("Обновленный список людей:")
    print(inimesed)

while True:
    command = input('Команды: 1, 2, 3, 4, 5, z ')
    if command == '1':
        inimene = input('Введите имя человека. ')
        print(get_pikkused(inimene, inimene_dict))
    elif command == '2':
        print(show_inf(inimene_dict))
    elif command == '3':
        print(koige_pikk_ja_koige_madal(inimene_dict))
    elif command == '4':
        print(keskmine_pikkus(inimene_dict))
    elif command == '5':
        delete_person(inimene_dict)
    elif command == 'z':
        break
    else:
        print('Неверная команда')