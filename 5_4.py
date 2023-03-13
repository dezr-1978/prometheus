'''


��������� ������� file_search(folder, filename),
��� ������ 2 ��������� -- ������ folder �� ����� filename,
�� ������� ����� -- ������ ���� �� ����� ��� ����� filename � �������� folder.

������� ��������� folder �������� ��������� �����:

������ -- �� ����� � �������, ���� 0-� ������� ������ ����� �����, � �� ���� ������ ������������ ��� ����� � ��� ����� (1 ���� = 1 �����-������� ������), ��� ������� �����, �� ��� ���� ��������������� ��������. �� � � ������� ������ ������ ����'�����, ���� �� ����� ���������� � ���� ��� �����, � ���� �� ��������, � ������� ���������� (��������� � �������� � �� �����, � ��� ������������� ����������� ����), ��������� "/".

�������, �� ����� ��� ����� � ����������. ��������� ������ �������� False, ���� ���� �� ��������.

���������
������ �������: file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt')
�������: 'C:/ideas.txt'
������ �������: file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'find.me')
�������: False
������ �������: file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')
�������: '/home/user2/desktop/new folder/hereiam.py'

����� �� ������������ � ���������� ��� ��� ���������� �������� False �� �����.

'''


def file_search(folder, filename):
        adress = False
        if filename in folder:
                adress = folder[0] + '/' + filename
        else:
                for i in folder:
                        if isinstance(i, list) == True:
                                if len(i) > 1:
                                        rec = file_search(i, filename)
                                        if rec != False:
                                                adress = folder[0] + '/' + rec
        return adress

print file_search(['C:'], 'crack.exe')
print file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt')
print file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'find.me')
print file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')
print file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt'), '-->C:/ideas.txt'
print file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], '-->find.me'), "-->False"
print file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py'), '-->/home/user2/desktop/new folder/hereiam.py'
print file_search(['C:'], 'crack.exe'), "-->False"
print file_search(['C:', '1.txt', '2.txt', '3.txt', '4.txt'], '4.txt'),"-->C:/4.txt"
print file_search(['C:', '1.txt', '2.txt', '3.txt', '4.txt'], '1.txt') ,"-->C:/1.txt"
print file_search(['D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me']], 'hey.py'], 'find.me'), "-->D:/tmp/new folder1/find.me"
print file_search(['/tmp', ['1', ['2', ['3', ['4', ['5', 'key1', 'key2', 'key3']]]]]], 'key3'), "-->/tmp/1/2/3/4/5/key3"
