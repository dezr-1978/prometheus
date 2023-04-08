'''
Вхідні дані: 3 дійсних числа a, b, c. Передаються в програму як аргументи командного рядка.
Результат роботи: рядок "triangle", якщо можуть існувати відрізки з такою довжиною та з них можна скласти трикутник, або "not triangle" -- якщо ні.
Наприклад
Вхідні дані: 10 20 30
Приклад виклику: python lab3_1.py 10 20 30
Результат: not triangle
Вхідні дані: 1 1 1
Приклад виклику: python lab3_1.py 1 1 1
Результат: triangle
Вхідні дані: 5.5 5.5 -2
Приклад виклику: python lab3_1.py 5.5 5.5 -2
Результат: not triangle
'''



import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a + b > c and b + c > a and a + c > b:
    print "triangle"
else:
    print "not triangle"
