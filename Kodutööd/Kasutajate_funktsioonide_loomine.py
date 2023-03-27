#���������� �������������� ��������
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
x = int(input('������� ������ ����� : '))
y = int(input('������� ������ ��c�� : '))
z = input('������� ���� (+, -, *, /) : ')
print (arithmetic(x, y, z))
print()

#���������� ���
def is_year_leap(year):
  if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
      return False
  else:
      return True
    
year = int(input("������� ���: "))
if is_year_leap(year):
    print("��� ����������")
else:
    print("��� �� ����������")
print()

#�������
def square(a):
    P = 4 * a
    S = a ** 2
    d = a * (2 ** 0.5)
    return P, S, d

a = float(input("������� ������� ��������: "))
if a > 0:
    result = square(a)
    print("\n", result[0], "- ��������","\n", result[1], "- �������","\n", result[2], "- ���������")
else:
    print("������� �� ����� ���� ������������� ��� ������ 0!")
print()

#������� ����
def season(month):
  if month in (12, 1, 2):
    return "����"
  elif month in (3, 4, 5):
    return "�����"
  elif month in (6, 7, 8):
    return "����"
  elif month in (9, 10, 11):
    return "�����"

month = int(input("�������� ����� ������: "))
result = season(month)
if month > 0 and month < 13:
  print("������ ����� ����������� ������� ���� -", result)
else:
  print("������ ������ �� ����������!")
print()

#���������� �����
def bank(a, years):
    stavka = 0.1
    x = a*(1+stavka)**years
    return x

a = float(input("������� �����, ������� ������ ������� - "))
years = float(input("�� ����� ���������� ��� ������ ������� ��������? ������� �����: "))
final = round(bank(a, years),2)
if a<=0 and years<=0:
  print("��� ������!")
else:
  print("�� ����� �� ���������", final, "����")
print()

#������� �����
def is_prime(n):
   if n < 2:
       return False
   if n == 2:
       return True
   #��������� ���������� ������ �� ����� n � ��������� ��������� � ���������� limit.
   limit = n**(1/2)
   #������������� ��������� �������� ��� �������� ����� while
   i = 2
   while i <= limit:
       if n % i == 0:
           return False
       i += 1
   return True
print(is_prime(int(input("������� �����: "))))
print()

#���������� ����
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

day = int(input("������� ���� ������: "))
month = int(input("������� ����� (������): "))
year = int(input("������� ���: "))

if date(day, month, year):
#{} - ��� �����������, � ������� ����� ������������� �������� ����������.
    print("���� {}-{}-{} �������� ��������������".format(day, month, year)) 
else:
#����� format ������������ ��� ������ ������������ ���������� ����������.
    print("���� {}-{}-{} ���������������".format(day, month, year)) 
print()

#XOR ����������
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
#������� ord(char) ���������� ������������� �������� (��� �������) ��� ���������� ������� char.
#������� chr(code) ��������� �������� ��������������: ��� ��������� ������������� �������� � ���������� ��������������� ������.

string = input("������� ��, ��� ������ �����������: ")
try:
    key = int(input("������� ����: "))
except ValueError:
    print("������: ���� ������ ���� ����� ������.")
    exit()

# ������������� ������
encrypted = XOR_cipher(string, key)

# �������������� ������������� ������ (��������� XOR_uncipher)
decrypted = XOR_uncipher(encrypted, key)

# ������� ��������� �� �����
print(f"�������� ������: {string}")
print(f"������������� ������: {encrypted}")
print(f"�������������� ������: {decrypted}")
