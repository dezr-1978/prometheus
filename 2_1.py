﻿'''
Вхідні дані: 3 дійсних числа -- аргументи командного рядка.
Вихідні дані: результат обчислення формули
Аргументи передаються в порядку, зазначеному у формулі, назви змінних можуть використовуватися будь-які.
Приклад
Вхідні дані: 1 1 0.25
Приклад виклику: python lab2_1.py 1 1 0.25
Результат: 1.59576912161
'''

import sys
import math

x = float(sys.argv[1])
μ = float(sys.argv[2])
σ = float(sys.argv[3])

f = (1 / (σ * math.sqrt(2 * math.pi))) * math.exp(-(x - μ) ** 2 / (2 * σ ** 2))


print f
