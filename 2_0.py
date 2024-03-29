'''
 Завдання для тренування
0 points possible (ungraded)

Вхідні дані: 2 невід'ємних дійсних числа a та b -- аргументи командного рядка. b не дорівнює 0.

Вихідні дані: дійсне число -- результат обчислення формули
формула в графічному записі

Приклад
Вхідні дані: 0 1
Приклад виклику: python test.py 0 1
Результат: 0.0
Вхідні дані: 0.5 10
Приклад виклику: python test.py 0.5 10
Результат: 0.688209837593

'''

import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])

x = math.sqrt(a * b) / (math.exp(a) * b) + a * math.exp(2*a/b)

print x
