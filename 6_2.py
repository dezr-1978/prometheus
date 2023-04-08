'''
��������� ������� encode_morze(text),
��� ������ 1 �������� -- �����,
�� ������� �����, ���� ������ ������� �������, �� ������� ���������� ������, ������������ ���������� ����� ����� ��� ����������� �������. ������� �� ���� �����, �� �� ������� �� ����������� �������, ����������. �������� ���� ���������.

Morze code

��� �������� ����������� �� ������� ���� ���������� ��������� ������ ������. ��������� ���� ������� ����� �������. ����� �� ���������� ������ ����� -- ���� ������, �� ������� � ���� -- 3 ������, �� ������� -- 7 ������. ������ ������� ������������ �������, �������� ��������. ����������� "�������" ��������� ��������� ������� � ������ ������� ����: �� �-� ������� ����������� "^", ���� � ��� ������ ���������� ������, � "_", ���� ������� ����. ���� ����� � ���� ����������� �� "������" �������.
'''

def encode_morze(text):
    
        morze_code = { "A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..", "E" : ".", "F" : "..-.", "G" : "--.",
                       "H" : "....", "I" : "..", "J" : ".---", "K" : "-.-", "L" : ".-..", "M" : "--", "N" : "-.",
                       "O" : "---", "P" : ".--.", "Q" : "--.-", "R" : ".-.", "S" : "...", "T" : "-", "U" : "..-",
                       "V" : "...-", "W" : ".--", "X" : "-..-", "Y" : "-.--", "Z" : "--.."}

        morze_simbol = {"." : "^", "-" : "^^^", " " : "_", "_" : "_", "___" : "_____"}

        simbol = morze_simbol.keys()
        text = text.upper()
        text = text.strip()
        l = []
        s = ''
        encode = ''
        
        for i in text:
                if i in morze_code:
                        l.append(morze_code.get(i))
                elif i == " ":
                        l.append("_")
        s = "_".join(l)

        for j in s:
                if j in simbol:
                        encode = encode + "_" +  morze_simbol[j]
        encode = encode[1: ]
        
        return encode
                


print encode_morze('Morze code')
print encode_morze('Prometheus')
print encode_morze('SOS')
print encode_morze('1')
print '---------'
print encode_morze('') == ''
print encode_morze('1.23') == ''
print encode_morze('HOUSTON WE HAVE A PROBLEM') == '^_^_^_^___^^^_^^^_^^^___^_^_^^^___^_^_^___^^^___^^^_^^^_^^^___^^^_^_______^_^^^_^^^___^_______^_^_^_^___^_^^^___^_^_^_^^^___^_______^_^^^_______^_^^^_^^^_^___^_^^^_^___^^^_^^^_^^^___^^^_^_^_^___^_^^^_^_^___^___^^^_^^^'
print encode_morze('In a hole in the ground there lived a hobbit') == '^_^___^^^_^_______^_^^^_______^_^_^_^___^^^_^^^_^^^___^_^^^_^_^___^_______^_^___^^^_^_______^^^___^_^_^_^___^_______^^^_^^^_^___^_^^^_^___^^^_^^^_^^^___^_^_^^^___^^^_^___^^^_^_^_______^^^___^_^_^_^___^___^_^^^_^___^_______^_^^^_^_^___^_^___^_^_^_^^^___^___^^^_^_^_______^_^^^_______^_^_^_^___^^^_^^^_^^^___^^^_^_^_^___^^^_^_^_^___^_^___^^^'
print encode_morze('Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.') == '^^^_^___^^^_^^^_^^^___^^^_______^_^^^_______^^^_^___^_^^^___^_^_^___^^^___^^^_^_^^^_^^^_______^^^_^_^___^_^___^_^^^_^___^^^___^^^_^_^^^_^^^_______^_^^^_^^^___^___^^^_______^_^_^_^___^^^_^^^_^^^___^_^^^_^_^___^_______^_^_^^^_^___^_^___^_^^^_^_^___^_^^^_^_^___^___^^^_^_^_______^_^^^_^^^___^_^___^^^___^_^_^_^_______^^^___^_^_^_^___^_______^___^^^_^___^^^_^_^___^_^_^_______^^^_^^^_^^^___^_^_^^^_^_______^_^^^_^^^___^^^_^^^_^^^___^_^^^_^___^^^_^^^___^_^_^_______^_^^^___^^^_^___^^^_^_^_______^_^^^___^^^_^_______^^^_^^^_^^^___^^^_^^^_^^^___^^^_^^^_^_^___^^^_^_^^^_^^^_______^_^_^___^^^_^^^___^___^_^^^_^_^___^_^^^_^_^_______^^^_^___^^^_^^^_^^^___^_^^^_^_______^^^_^_^^^_^^^___^___^^^_______^_^^^_______^^^_^_^___^_^^^_^___^^^_^_^^^_^^^_______^^^_^_^_^___^_^^^___^_^^^_^___^_______^_^_^___^_^^^___^^^_^___^^^_^_^___^^^_^_^^^_^^^_______^_^_^_^___^^^_^^^_^^^___^_^^^_^_^___^_______^_^^^_^^^___^_^___^^^___^_^_^_^_______^^^_^___^^^_^^^_^^^___^^^___^_^_^_^___^_^___^^^_^___^^^_^^^_^_______^_^___^^^_^_______^_^___^^^_______^^^___^^^_^^^_^^^_______^_^_^___^_^___^^^_______^^^_^_^___^^^_^^^_^^^___^_^^^_^^^___^^^_^_______^^^_^^^_^^^___^^^_^_______^^^_^^^_^^^___^_^^^_^_______^^^___^^^_^^^_^^^_______^___^_^^^___^^^_______^_^___^^^_______^_^^^_^^^___^_^^^___^_^_^_______^_^^^_______^_^_^_^___^^^_^^^_^^^___^^^_^_^_^___^^^_^_^_^___^_^___^^^___^_^_^_^___^^^_^^^_^^^___^_^^^_^_^___^_______^_^^^___^^^_^___^^^_^_^_______^^^___^_^_^_^___^_^^^___^^^_______^^^_^^^___^___^_^^^___^^^_^___^_^_^_______^^^_^_^^^_^___^^^_^^^_^^^___^^^_^^^___^_^_^^^_^___^^^_^^^_^^^___^_^^^_^___^^^'
 