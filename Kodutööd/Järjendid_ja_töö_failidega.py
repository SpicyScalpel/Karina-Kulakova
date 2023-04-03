#�������� ������� inimesed(), ��� ������� ������� ���������� ���������� ���� �������: ����[], ����[]. 
#���������� ��������� � ������� �������������� ������������� (���� ������������� ������� ����� ���� ��������, ���� � ������ online- ������ �������� ���� �� ���������� ������ � �����).
#����� ���������� �������� ���������� ���� � ������� ��������:
#� ���� �������;
#� ���������� � ���������� ������� ������ ����� � �� ����;
#� ����� ������ �������� � ������ ������� �� �����;
#� ����� ������� ���� n ����� � ������, ����� ����� ������ ������������ ;
#� ������� �� ������ �������� � ������ � ��� �����, ����� ��� ��������
#��� �������� �������� �������� ����������� �������.

# ������� ������ ������ ��� �������� ���� � �����
inimesed = []
pikkused = []

# ��������� ���� ��� ����� ������ � �����
while True:
    # ������ ��� ��������
    inimene = input('������� ��� ��������. ')
    # ������ ���� ��������
    pikkus = int(input('������� ���� ����� ��������. '))
    # ��������� ��� � ���� � ��������������� ������
    inimesed.append(inimene)
    pikkused.append(pikkus)
    # ���������, ����� �� ������������ ��������� ���� ������
    log_out = input('������� "z" ��� ���������� ����� ������ � ����� \
��� Enter ��� �����������. ')
    if log_out.lower() == 'z':
        break
print("C����� �����:")
print(inimesed)

# ������� �������, ��� ����� - �����, � �������� - ����
inimene_dict = dict(zip(inimesed, pikkused))

# ������� ��� ��������� ����� �������� �� �����
def get_pikkused(inimene, inimesed):
    if inimene in inimesed.keys():
        return f'���� {inimene} ����� {inimesed[inimene]} ��.'
    else:
        return '������ �������� ��� � ������.' 

# ������� ��� ������ ���������� � ����� � ���������� ������� �� �����
def show_inf(inimesed):
    sorted_tuple = sorted(inimesed.items())
    return sorted_tuple

# ������� ��� ������ ������ �������� � ������ ������� �������� � ������
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
    return f'����� ������� �������: {isik_max} ({pikk_max} ��), ����� ������ �������: {isik_min} ({pikk_min} ��)'

# ������� ��� ���������� �������� ����� �����
def keskmine_pikkus(inimesed):
    # ������� ���������� ����� ��� �������
    n = int(input("������� ���������� �����: "))
    
    pikkused = [] # ������ ������ �����
    
    for i in range(n):
        nimi = input(f"������� ��� {i+1}-�� ��������: ")
        pikkus = inimesed[nimi]
        pikkused.append(pikkus)
    
    # ������ ������� ����
    sum_pikkused = sum(pikkused)
    kesk_pikkus = sum_pikkused / n
    
    return f'������� ���� �����: {kesk_pikkus:.2f} ��.'

 
def delete_person(inimesed):
    inimene = input("������� ��� �������� ��� ��������: ")
    if inimene in inimesed:
        del inimesed[inimene]
        print(f"{inimene} ������(�) �� ������")
    else:
        print(f"{inimene} �� ������(�) � ������")

    print("����������� ������ �����:")
    print(inimesed)

while True:
    command = input('�������: 1, 2, 3, 4, 5, z ')
    if command == '1':
        inimene = input('������� ��� ��������. ')
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
        print('�������� �������')