'''
Розробити класс Student для представлення відомостей про успішність слухача курсу Prometheus. Об'єкт класу має містити поля для збереження імені студента та балів, отриманих ним за виконання практичних завдань і фінального екзамена.
Забезпечити наступні методи класу:
конструктор, який приймає рядок -- ім'я студента -- та словник, що містить налаштування курсу у наступному форматі:
conf = {
'exam_max': 30, # кількість балів, доступна за здачу екзамена
'lab_max': 7, # кількість балів, доступна за виконання 1 практичної роботи
'lab_num': 10, # кількість практичних робіт в курсі
'k': 0.61, # частка балів від максимума, яку необхідно набрати для отримання сертифікату
}.
метод make_lab(m,n), який приймає 2 аргументи та повертає посилання на поточний об'єкт. Тут m -- кількість балів набрана за виконання завдання (ціле або дійсне число), а n -- ціле невід'ємне число, порядковий номер завдання (лаби нумеруються від 0 до lab_num-1). При повторній здачі завдання зараховується остання оцінка. Якщо n не задане, мається на увазі здача першого невиконаного практичного завдання. Врахувати, що під час тестування система іноді дає збої, тому за виконання завдання може бути нараховано більше балів ніж це можливо за правилами курсу, що не повинно впливати на рейтинг студента. Крім того в системі можуть міститися додаткові завдання, чиї номери виходять за межі 0..lab_num -- звичайно, бали за них не повинні зараховуватися для отримання сертифікату.
метод make_exam(m), який приймає 1 аргумент -- ціле або дійсне число, оцінку за фінальний екзамен, та повертає посилання на поточний об'єкт. Як і у випадку з практичними завданнями, оцінка за екзамен в результаті помилки іноді може перевищувати максимально допустиму.
метод is_certified(), який повертає тьюпл, що містить дійсне число (суму балів студента за проходження курсу), та логічне значення True або False в залежності від того, чи достатньо цих балів для отримання сертифікату.
Так як курс є доступним онлайн і не має дедлайнів на здачу робіт, студент може виконувати роботи в довільному порядку. Вважати, що кількість спроб на виконання кожного з завдань необмежена.
Приклад послідовності дій для тестування класу:
conf = {
'exam_max': 30,
'lab_max': 7,
'lab_num': 10,
'k': 0.61,
}
oleg = Student('Oleg', conf)
oleg.make_lab(1) \ # labs: 1 0 0 0 0 0 0 0 0 0, exam: 0
.make_lab(8,0) \ # labs: 7 0 0 0 0 0 0 0 0 0, exam: 0
.make_lab(1) \ # labs: 7 1 0 0 0 0 0 0 0 0, exam: 0
.make_lab(10,7) \ # labs: 7 1 0 0 0 0 0 7 0 0, exam: 0
.make_lab(4,1) \ # labs: 7 4 0 0 0 0 0 7 0 0, exam: 0
.make_lab(5) \ # labs: 7 4 5 0 0 0 0 7 0 0, exam: 0
.make_lab(6.5) \ # labs: 7 4 5 6.5 0 0 0 7 0 0, exam: 0
.make_exam(32) # labs: 7 4 5 6.5 0 0 0 7 0 0, exam: 30
print oleg.is_certified() # (59.5, False)
oleg.make_lab(7,1) # labs: 7 7 5 6.5 0 0 0 7 0 0, exam: 30
print oleg.is_certified() # (62.5, True)
'''

class Student(object):
    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        self.labs = [0] * self.conf.get('lab_num')
        self.exam = 0.0

    def make_lab(self, m, n=-1):

        if n >= self.conf.get('lab_num'):
            return self

        if n == -1:
            try:
                n = self.labs.index(0)
            except:
                return self

        if m > self.conf.get('lab_max'):
            m = self.conf.get('lab_max')

        self.labs[n] = m 

        return self


    def make_exam(self, m):
        if m > self.conf.get('exam_max'):
            m = self.conf.get('exam_max')
        self.exam = m
        return self

    def is_certified(self):
        smarks = sum(self.labs) + self.exam
        
        if smarks/100.0 >= self.conf.get('k'):
            is_cert = True
        else:
            is_cert = False
        return (smarks, is_cert)



conf1 = {'exam_max': 20,'lab_max': 40,'lab_num': 2,'k': 0.75}
o1 = Student('Oleg', conf1)
print(o1.is_certified(), '(0, False)')
o2 = Student('Oleg', conf1)
o2.make_lab(60).make_lab(35.2)
print(o2.is_certified(), '(75.2, True)')
o3 = Student('Oleg', conf1)
o3.make_lab(10).make_lab(10).make_exam(15)
print(o3.is_certified(), '(35, False)')
o3.make_lab(20,1).make_lab(20,0)
print(o3.is_certified(), '(55, False)')
o3.make_lab(50,2)
print(o3.is_certified(), '(55, False)')
o3.make_lab(40,1)
print(o3.is_certified(), '(75, True)')
conf2 = {'exam_max': 52,'lab_max': 8,'lab_num': 6,'k': 0.5}
o4 = Student('Oleg', conf2)
o4.make_exam(100)
print(o4.is_certified(), '(52, True)')
o5 = Student('Oleg', conf2)
o5.make_lab(40).make_lab(7,5).make_lab(1).make_lab(7).make_lab(7).make_lab(7).make_lab(7,1)
print(o5.is_certified(), '(43, False)')
o5.make_lab(7)
print(o5.is_certified(), '(43, False)')
o5.make_exam(7)
conf3 = {'exam_max': 10,'lab_max': 1,'lab_num': 90,'k': 0.5,}
o6 = Student('Oleg', conf3)
for i in range(51): o6.make_lab(1)
print(o6.is_certified(), '(51, True)')
