'''
����� ���: 3 ������ ����� a, b, c. ����������� � �������� �� ��������� ���������� �����.
��������� ������: ����� "triangle", ���� ������ �������� ������ � ����� �������� �� � ��� ����� ������� ���������, ��� "not triangle" -- ���� �.
���������
����� ���: 10 20 30
������� �������: python lab3_1.py 10 20 30
���������: not triangle
����� ���: 1 1 1
������� �������: python lab3_1.py 1 1 1
���������: triangle
����� ���: 5.5 5.5 -2
������� �������: python lab3_1.py 5.5 5.5 -2
���������: not triangle
'''

import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a + b > c and b + c > a and a + c > b:
    print "triangle"
else:
    print "not triangle"
