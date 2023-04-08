'''
��������� ������� find_most_frequent(text), 
��� ������ 1 �������� -- ����� ������� �������, ���� ���� ������ ����� ����������� �������, ������ �� ������� ����� (,.:;!?-); 
�� ������� ������ ��� (� �������� ������), �� ������������ � ����� ���������.
�����, ������� ����� �����, ������� ����� ������� (���������, "hand-made"). ����� � ����� �������, ������ �� � ������ �������������� (���������, "page" �� "pages") ���������� ������ �������. ������ ��� -- �������, �� �� ��������: ����� "page" �� "Page" ���������� 1 ������.
���� ���, �� ������������ ���������, ������� -- ������� �� � ���������� �������.
���������
������ �������: find_most_frequent('Hello,Hello, my dear!')
�������: ['hello']
������ �������: find_most_frequent('to understand recursion you need first to understand recursion...')
�������: ['recursion', 'to', 'understand']
������ �������: find_most_frequent('Mom! Mom! Are you sleeping?!!!')
�������: ['mom']
'''

def find_most_frequent(text):

    symbols = [',','.',':',';','!','?','-',' ']
    list_mark = ''  
    words = [] 
    list_c = [] 
    most_frequent = [] 
    for i in range(len(text.lower())): 
        if text.lower()[i] in symbols:
             list_mark = list_mark + '*' 
        else:
             list_mark = list_mark + text.lower()[i] 
    words = list_mark.split('*') 

    for i in range(len(words)):
        if len(words[i]) < 1 or words[i] in words[:i]: 
            list_c.append(0)
        else:
            list_c.append(words.count(words[i]))
    for i in range(len(list_c)):
        if list_c[i] == max(list_c):
            most_frequent.append(words[i])

    most_frequent.sort()
    if text == '':
        return []
    else:
        return most_frequent


print (find_most_frequent('Mike-Paul mike')), ['mike']
print (find_most_frequent("Load up on guns; bring your friends It's fun to lose and to pretend She's over-bored and self-assured Oh no, I know a dirty word Hello,hello,hello,how low Hello,hello,hello,howlow Hello,hello,hello,how low Hello,hello,hello")), ['hello']
print (find_most_frequent("And I forget just why I taste; Oh yeah, I guess it makes me smile; I found it hard; it's hard to find; Oh well, whatever, never mind")), ['i']
print (find_most_frequent('This is the front page of the Simple English Wikipedia. Wikipedias are places where people work together to write encyclopedias in different languages. We use Simple English words and grammar here. The Simple English Wikipedia is for everyone! That includes children and adults who are learning English. There are 120,571 articles on the Simple English Wikipedia. All of the pages are free to use. They have all been published under both the Creative Commons Attribution/Share-Alike License 3.0 and GNU Free Documentation License. You can help here! You may change these pages and make new pages. Read help pages and other good pages to learn how to write pages here. If you need help, you may ask questions at Simple talk.')), ['pages', 'the']

print (find_most_frequent('Hello,Hello, my dear!')), ['hello']
print (find_most_frequent('to understand recursion you need first to understand recursion...')), ['recursion', 'to', 'understand']
print (find_most_frequent('Mom! Mom! Are you sleeping?!!!')), ['mom']


print find_most_frequent('Mike-Paul mike'), ['mike']
print find_most_frequent("Load up on guns; bring your friends It's fun to lose and to pretend She's over-bored and self-assured Oh no, I know a dirty word Hello,hello,hello,how low Hello,hello,hello,howlow Hello,hello,hello,how low Hello,hello,hello"), ['hello']
print find_most_frequent("And I forget just why I taste; Oh yeah, I guess it makes me smile; I found it hard; it's hard to find; Oh well, whatever, never mind"), ['i']
print find_most_frequent('This is the front page of the Simple English Wikipedia. Wikipedias are places where people work together to write encyclopedias in different languages. We use Simple English words and grammar here. The Simple English Wikipedia is for everyone! That includes children and adults who are learning English. There are 120,571 articles on the Simple English Wikipedia. All of the pages are free to use. They have all been published under both the Creative Commons Attribution/Share-Alike License 3.0 and GNU Free Documentation License. You can help here! You may change these pages and make new pages. Read help pages and other good pages to learn how to write pages here. If you need help, you may ask questions at Simple talk.'), ['pages', 'the']

print find_most_frequent('Hello,Hello, my dear!'), ['hello']
print find_most_frequent('to understand recursion you need first to understand recursion...'), ['recursion', 'to', 'understand']
print find_most_frequent('Mom! Mom! Are you sleeping?!!!'), ['mom']

print find_most_frequent('This is the front page of the Simple English Wikipedia. Wikipedias are places where people work together to write encyclopedias in different languages. We use Simple English words and grammar here. The Simple English Wikipedia is for everyone! That includes children and adults who are learning English. There are 120,571 articles on the Simple English Wikipedia. All of the pages are free to use. They have all been published under both the Creative Commons Attribution/Share-Alike License 3.0 and GNU Free Documentation License. You can help here! You may change these pages and make new pages. Read help pages and other good pages to learn how to write pages here. If you need help, you may ask questions at Simple talk.')
print find_most_frequent("Load up on guns; bring your friends It's fun to lose and to pretend She's over-bored and self-assured Oh no, I know a dirty word Hello,hello,hello,how low Hello,hello,hello,howlow Hello,hello,hello,how low Hello,hello,hello") 
print find_most_frequent("And I forget just why I taste; Oh yeah, I guess it makes me smile; I found it hard; it's hard to find; Oh well, whatever, never mind")
