'''
Вхідні дані: довільна, відмінна від нуля, кількість значень - аргументів командного рядка. Значеннями-аргументами можуть бути числа або рядки, які складаються з цифр та літер латинського алфавіту без пробілів.
Результат роботи: рядок, що складається з отриманих значень в зворотньому порядку, записаних через пробіл. Пробіл в кінці рядка відсутній.
Наприклад
Вхідні дані: 1
Приклад виклику: python lab4_3.py 1
Результат: 1
Вхідні дані: qwe asd zxc 123
Приклад виклику: python lab4_3.py qwe asd zxc 123
Результат: 123 zxc asd qwe
Вхідні дані: padawan young my HAVE MUST YOU PATIENCE
Приклад виклику: python lab4_3.py padawan young my HAVE MUST YOU PATIENCE
Результат: PATIENCE YOU MUST HAVE my young padawan
'''

import sys

x_list = list(sys.argv[1:])

x_list.reverse()
x_list = ' '.join(x_list)

print x_list
