'''
����� ���: �������, ������ �� ����, ������� ������� - ��������� ���������� �����. ����������-����������� ������ ���� ����� ��� �����, �� ����������� � ���� �� ���� ����������� ������� ��� ������.
��������� ������: �����, �� ���������� � ��������� ������� � ����������� �������, ��������� ����� �����. ����� � ���� ����� �������.
���������
����� ���: 1
������� �������: python lab4_3.py 1
���������: 1
����� ���: qwe asd zxc 123
������� �������: python lab4_3.py qwe asd zxc 123
���������: 123 zxc asd qwe
����� ���: padawan young my HAVE MUST YOU PATIENCE
������� �������: python lab4_3.py padawan young my HAVE MUST YOU PATIENCE
���������: PATIENCE YOU MUST HAVE my young padawan
'''

import sys

x_list = list(sys.argv[1:])

x_list.reverse()
x_list = ' '.join(x_list)

print x_list
