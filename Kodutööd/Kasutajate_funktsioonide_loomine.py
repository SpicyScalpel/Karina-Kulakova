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
