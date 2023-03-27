#Простейшие арифметические операции
def arithmetic (x, y, z):
	if z == "+" :
		return (x + y)
	elif z == "-":
		return (x - y)
	elif z == "*":
		return (x * y)
	elif z == "/":
		return (x / y)
	else :
		return ("Invalid operation")
x = int(input('Введите первое число : '))
y = int(input('Введите второе чиcло : '))
z = input('Введите знак (+, -, *, /) : ')
print (arithmetic(x, y, z))
print()

#Високосный год
def is_year_leap(year):
  if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
      return False
  else:
      return True
    
year = int(input("Введите год: "))
if is_year_leap(year):
    print("Год високосный")
else:
    print("Год не високосный")
print()

#Квадрат
def square(a):
    P = 4 * a
    S = a ** 2
    d = a * (2 ** 0.5)
    return P, S, d

a = float(input("Введите сторону квадрата: "))
if a > 0:
    result = square(a)
    print("\n", result[0], "- Периметр","\n", result[1], "- Площадь","\n", result[2], "- Диагональ")
else:
    print("Сторона не может быть отрицательной или равной 0!")
print()

#Времена года
def season(month):
  if month in (12, 1, 2):
    return "зима"
  elif month in (3, 4, 5):
    return "весна"
  elif month in (6, 7, 8):
    return "лето"
  elif month in (9, 10, 11):
    return "осень"

month = int(input("Напишите месяц цифрой: "))
result = season(month)
if month > 0 and month < 13:
  print("Данный месяц принадлежит времени года -", result)
else:
  print("Такого месяца не существует!")
print()

#Банковский вклад
def bank(a, years):
    stavka = 0.1
    x = a*(1+stavka)**years
    return x

a = float(input("Введите сумму, которую хотите вложить - "))
years = float(input("На какое количество лет хотите сделать вложение? Введите число: "))
final = round(bank(a, years),2)
if a<=0 and years<=0:
  print("Так нельзя!")
else:
  print("По итогу вы получаете", final, "евро")
print()

#Простые числа
def is_prime(n):
   if n < 2:
       return False
   if n == 2:
       return True
  #вычисляем квадратный корень из числа n и результат сохраняем в переменную limit.
   limit = n**(1/2)
   #устанавливаем начальное значение для счетчика цикла while
   i = 2
   while i <= limit:
       if n % i == 0:
           return False
       i += 1
   return True
print(is_prime(int(input("Введите число: "))))
print()

#Правильная дата
def is_year_leap(year):
  if (year %4 ==0) and (year % 100 !=0) or (year % 400 ==0):
    return True
  return False

def date(day, month, year):
  if (type(day + month + year) != int):
    return False
  if (month<=0 or month >12):
    return False
  if (day <=0 or day >31):
    return False
  if (year <0):
    return False
  if (month==2):
    if(is_year_leap(year) and (day>29)):
      return False
    if(not is_year_leap(year) and (day>28)):
      return False
  return True

day = int(input("Введите день месяца: "))
month = int(input("Введите месяц (цифрой): "))
year = int(input("Введите год: "))

if date(day, month, year):
#{} - это заполнители, в которые будут подставляться значения переменных.
    print("Дата {}-{}-{} является действительной".format(day, month, year)) 
else:
#Метод format используется для замены заполнителей значениями переменных.
    print("Дата {}-{}-{} недействительна".format(day, month, year)) 
print()

#XOR шифрование
def XOR_cipher(string, key):
    encrypt_string = ''
    for char in string:
        encrypt_string += chr(ord(char) ^ key)
    return encrypt_string
  
def XOR_uncipher(string, key):
    decrypted_string = ''
    for char in string:
        decrypted_string += chr(ord(char) ^ key)
    return decrypted_string
#Функция ord(char) возвращает целочисленное значение (код символа) для указанного символа char.
#Функция chr(code) выполняет обратное преобразование: она принимает целочисленное значение и возвращает соответствующий символ.

string = input("Введите то, что хотите зашифровать: ")
try:
    key = int(input("Введите ключ: "))
except ValueError:
    print("Ошибка: ключ должен быть целым числом.")
    exit()

# зашифровываем строку
encrypted = XOR_cipher(string, key)

# расшифровываем зашифрованную строку (используя XOR_uncipher)
decrypted = XOR_uncipher(encrypted, key)

# выводим результат на экран
print(f"Исходная строка: {string}")
print(f"Зашифрованная строка: {encrypted}")
print(f"Расшифрованная строка: {decrypted}")
