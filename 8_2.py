'''
Розробити функцію find_fraction(summ), 
яка приймає 1 аргумент -- невід'ємне ціле число summ, 
та повертає тьюпл, що містить 2 цілих числа -- чисельник та знаменник найбільшого правильного нескорочуваного дробу, для якого сума чисельника та знаменника дорівнює summ. Повернути False, якщо утворити такий дріб неможливо.
Тести із некоректними даними не проводяться.
Приклад послідовності дій для тестування:
print find_fraction(2) # False
print find_fraction(3) # (1, 2)
print find_fraction(10) # (3, 7)
print find_fraction(62) # (29, 33)
print find_fraction(150000001) # (75000000, 75000001)

'''
def find_fraction(summ):

	x = summ / 2.0
	if summ == 0:
		return False

	if summ % 2:
		a, b = x - 0.5, x + 0.5
	else:
		if x % 2:
			a, b = x - 2, x + 2
		else:
			a, b = x -1, x + 1

	if (a > 0 and b > 0):
		return (int(a), int(b))
	else:
		return False

print find_fraction(2) # False
print find_fraction(3) # (1, 2)
print find_fraction(10) # (3, 7)
print find_fraction(62) # (29, 33)
print find_fraction(150000001) # (75000000, 75000001)
