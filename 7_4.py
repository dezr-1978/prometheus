
'''
��������� ������� create_calendar_page(month,year), 
��� ������ 2 ��������� -- ��� ����� -- ����� (��������� ���������� � 1) � ��, 
�� ������� ���������� return 1 �����, ���� ������ ������� ��������� �� ��� �����.
���� ����� �� �� �� �����, ����������� ��������� ��������.
"�������", �� �����������, �� ��������� ������:
������� ����������
�� �������� � ����� ������ �� ���������� ����� \n, ������ ���� ����� 28 ������. ���� ������ � ���� ��-����� ��� ������ �����, �� � ���� ������ ����� ����������.
����� �� ������������ ������ �� �����������.
������� ������� ��� ���������� �������:
print create_calendar_page(1)
print create_calendar_page()
print create_calendar_page(3)
print create_calendar_page(04, 1992)
'''

def create_calendar_page(month=4, year = 2023):
    import calendar
    
    dt = ''
    pl = '--------------------\nMO TU WE TH FR SA SU\n--------------------\n'
    weekdays = calendar.Calendar()
    for i in weekdays.monthdayscalendar(year, month):
        for q in i:
            q = str(q)
            if q == 0:
                q = q.replace('0', ' ')
            if len(q) == 1:
                q = '0' + q
            dt += q + ' '
        dt = dt + '\n'
    
    dt = dt.replace(' \n', '\n')
    dt = dt.replace('00', '  ')
    
    return pl + dt

print create_calendar_page()    

