#XOR 
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
