'''

��������� ������� clean_list(list_to_clean),
��� ������ 1 �������� -- ������ ����-���� ������� (�����, ����� �� ������ �����) ������� �������,
�� ������� ������, ���� ���������� � ��� ����� �������, ��� �� ������ ������� ��������. �� �������, �� � ������� �������� �������� � ����������� ������ � ������ ����������� ������ "���������" �������� ���������� �� ����� ����, � ������, ����� �� ��. �����������.

���������
������ �������: clean_list([1, 1.0, '1', -1, 1])
�������: [1, 1.0, '1', -1]
������ �������: clean_list(['qwe', 'reg', 'qwe', 'REG'])
�������: ['qwe', 'reg', 'REG']
������ �������: clean_list([32, 32.1, 32.0, -123])
�������: [32, 32.1, 32.0, -123]
������ �������: clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5])
�������: [1, 2, 3, 4, 5, 6, '2', 7, 8, 9, 0]

'''
import sys

l = list(sys.argv[1:])
b=[]

def clean_list(l):
    for i in l:
        for j in b:
            if i==j and type(i)==type(j):
                break
        else:
            b.append(i)
    return b

print clean_list(l)
