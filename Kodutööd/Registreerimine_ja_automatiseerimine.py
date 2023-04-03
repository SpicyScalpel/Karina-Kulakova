from random import *
from sys import * # Программа выходит с кодом возврата 0 (успешное завершение), также имеется программа argv и другие

kasutajanimi_list = ["kasutaja1","kasutaja2","kasutaja3","kasutaja4"]
parool_list = ["par1","par2","par3","par4"]
def parooli_generatsioon(number_of_initials:int):
    """Parooli isegenereerimine
    Args:
        number_of_initials (int): _sümbolite arv_
    Returns:
        _type_: _tagastab uus parrol_
    """
    
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3 
    ls = list(str4)
    shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    parool = ''.join([choice(ls) for x in range(number_of_initials)])
    # Пароль готов
    print("Sinu genereeritud salasõna on: ", parool)
    return parool

def kasutaja_valikud():
    """Funktsioon annab kasutajale valik: kas sisseloogida voi registreeruda
    """
    print("Tere! \nPalun registreeri või logi sisse!!")
    #Использование try-except позволяет обрабатывать исключения в программе, что делает ее более надежной и устойчивой к ошибкам.
    while True:
        try:
            valik = int(input("\nKui soovid luua uut kontot - sisesta number 1, kui soovid sisse logida - sisesta number 2, kui soovid väljuda - sisesta number 3 --> "))
        except:
            print("Sisesta number!")
        if str(valik) == "2":
            kasutaja_login()
        elif str(valik) == "1":
            kasutaja_reg()
            kasutaja_login()
        elif str(valik) == "3":
            print("Head aega!")
            exit()

def kasutaja_login():
    """Funktsioon teeb sisselogimis protsessi
    """
    kasutaja = input("\nTere!\nPalun sisesta oma kasutajanimi --> ")
    try:
        if kasutaja in kasutajanimi_list:
            #Поиск индекса элемента kasutaja в списке kasutajanimi_list и сохранение его в переменную a.
            a = kasutajanimi_list.index(kasutaja) 
            for i in range(3):
                parool = input(f"\n,{kasutaja}!\nPalun sisesta oma parooli --> ")
                if parool == kasutajanimi_list[a]: 
                    print("\nEdukalt sisse logitud!")
                    break
                else:
                    print("\nVale parool!",(1+i))         
        else:
            for i in range(3):
                print("\nVale kasutajanimi!")
                kasutaja = input("\nPalun sisesta õige kasutajanimi --> ")
                if kasutaja in kasutajanimi_list:
                    a = kasutajanimi_list.index(kasutaja)
                    break
                else: 
                    print("\nVale! Palun sisesta õige number: ", i+1)
                    if i == 3:
                        break     
    except:
        print("Viga!")
              
def kasutaja_reg():
    """Kasutaja loob endale uus konto.
    Returns:
        _type_: tagastab password
    """
    kasutaja = input("Palun sisesta uus kasutajanimi --> ")
    while kasutaja in kasutajanimi_list:
        print("See kasutajanimi on juba kasutusel! Palun vali mõni teine nimi.")
        kasutaja = input("Palun sisesta uus kasutajanimi --> ")
    else:    
        #Данная строка кода добавляет переменную kasutaja в конец списка kasutajanimi_list.
        kasutajanimi_list.append(kasutaja)
    salasona = int(input("Kui soovid genereerida parooli - sisesta number 1, kui soovid kasutada oma parooli - sisesta number 2 --> "))
    if salasona == "1":
        try:
            arv = int(input("Palun sisesta algne summa --> "))
        except:
            print("Sa pead sisestama numbri!")
        parool_list.append(parooli_generatsioon(arv))
    elif salasona == "2":
        parool = input("Palun sisesta uus parool --> ")
        while parooli_kontrollimine(parool) == False:
            parool = input("Palun sisesta uus parool --> ") 
        if parooli_kontrollimine(parool) == True:
            parool_list.append(str(parool))
            print("\nSinu uus parool on: ", str(parool))
    return parool_list
        
def parooli_kontrollimine(parool:str):
    """Func kontrollib salasona.
    Args:
        parool (str): _salasona mis paneb ise kasutaja_
    Returns:
        _type_: tagastab True or False.
    """
    parool = list(parool)
    #3 переменные, «a», «b» и «c», равные 0, которые будут использоваться для подсчета количества цифр, заглавных букв и букв в пароле 
    arv = len(parool)
    a = 0
    b = 0
    c = 0
    for i in range(arv):
        #Перебираем каждый символ в пароле и проверяем, является ли он цифрой, заглавной буквой или буквой. Если да, то добавляем +1 к определенной переменной
        #isdigit() -kontrollib, kas on muutuja arv ja tagastab True või False
        if parool[i].isdigit():
            a += 1
        else:
            a += 0
        #isupper() - kontrollib, kas oli sisestatud suurtähtedega muutuja
        if parool[i].isupper():
            b += 1
        else:
            b += 0
        #isalpha() - проверяет состоит ли строка только из буквенных символов или нет
        if parool[i].isalpha() == True:
            c += 1
        else:
            c += 0
    #Проверяем, все ли «a», «b» и «c» больше 0.
    if a > 0 and b > 0 and c > 0:
        return True
    else:
        print("Parool peab koosnema numbritest, tähtedest ja suurtähtedest!")
        return False

kasutaja_valikud()
