'''


Розробити функцію count_holes(n),
яка приймає 1 аргумент -- ціле число або рядок, який містить ціле число,
та повертає ціле число -- кількість "отворів" у десятковому записі цього числа друкованими цифрами (вважати, що у "4" та у "0" по одному отвору), або рядок ERROR, якщо переданий аргумент не задовольняє вимогам: є дійсним або взагалі не числом.

пояснення щодо отворів в цифрах

Незначущими нулями на початку запису числа, якщо такі є, нехтувати.

Наприклад
Виклик функціїі: count_holes('123')
Повертає: 0
Виклик функціїі: count_holes(906)
Повертає: 3
Виклик функціїі: count_holes('001')
Повертає: 0
Виклик функціїі: count_holes(-8)
Повертає: 2
Виклик функціїі: count_holes(-8.0)
Повертає: ERROR

'''

def count_holes(n):
    
    d = {'9':1, '8':2, '7':0, '6':1, '5':0, '4':1, '3':0, '2':0, '1':0, '0':1}
    
    if type(n) != float:
        x = 0
        n = int(n)
        n = str(n)
        for i in n:
            if i in d:
                x += d.get(i)
    else:
        return 'ERROR'
        
    return x
  
print count_holes('123')
print count_holes(906)
print count_holes('001')
print count_holes(-8)
print count_holes(-8.0)
        
print count_holes('123'), '0'
print count_holes(906), '3'
print count_holes('001'), '0'
print count_holes(-8), "2"
print count_holes(-8.0), "ERROR"
print '---'
print count_holes(0), "1"
print count_holes(888888888888888888888), "42"
print count_holes(-888888888888888888888), "42"
print count_holes(69L), "2"
print count_holes('000000000010'), "1" 
print count_holes('888888888888888888888.0'), "ERROR"
print count_holes(''), "ERROR"
print count_holes([1]), "ERROR"
print count_holes(None), "ERROR"
print count_holes('qq'), "ERROR"



