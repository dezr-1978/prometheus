'''


��������� ������� super_fibonacci(n, m),
��� ������ 2 ��������� -- ������� ��� ����� n �� m (0 < n, m <= 35),
�� ������� ����� -- n-� ������� ����������� �����-Գ������� ������� m.

��������, �� ������������ Գ������� -- �� ������������ �����, � ��� ������ ������� ������� ��� ���� ����������. ������������ �����-Գ������� ������� m ������ ������� ���� ������������ �����, � ��� ������ ������� ������� ��� m ����������. ����� m �������� (� ����������� �������� �� 1 �� m) ����������� ���������.

���������
������ �������: super_fibonacci(2, 1)
�������: 1
������ �������: super_fibonacci(3, 5)
�������: 1
������ �������: super_fibonacci(8, 2)
�������: 21
������ �������: super_fibonacci(9, 3)
�������: 57

'''

import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

def super_fibonacci(n, m):
        f = []
        for i in range(n):
                if i < m:
                    f.append(1)
                else:
                    f.append(sum(f[-m:]))
        return f[n-1]

print super_fibonacci(n, m)

