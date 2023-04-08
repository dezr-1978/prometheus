'''
��������� ����� CombStr ��� ������������� ����� �������.
����������� ������� ������ �����:
�����������, ���� ������ 1 �������� -- ����� string.
����� count_substrings(length), ���� ������ 1 �������� -- ����'���� ���� ����� length, �� ������� ���� ����� -- ������� ��� ����� ������� �������� length, �� �������� � ����� string.
����� �� ������������ ������ �� �����������.
����������� ������� substring ��������� �������� ����� string, ���� �� ����� �������� � string ������ ��������� ������� � ������� ��/��� � ���� �����. ��������� 'asd' � �������� 'asdfg', � 'fgh' -- �. �������, �� ������� ������� �� ����, ���� ��� length=0 ��������� 0.
������� ����������� �� ��� ���������� �����:
s0 = CombStr('qqqqqqweqqq%')
print s0.count_substrings(0) # 0
print s0.count_substrings(1) # 4
print s0.count_substrings(2) # 5
print s0.count_substrings(5) # 7
print s0.count_substrings(15) # 0
'''

class CombStr(object):
	def __init__(self, string):
		self.string=string
		
	def count_substrings(self, length):
		self.length=length
		if self.length == 0:
			return 0
		a=0
		l=[]
		while self.length < len(self.string)+1:
			if self.string[a:self.length] not in l:
				l.append(self.string[a:self.length])
			a+=1; self.length+=1
		return len(l)

s0 = CombStr('qqqqqqweqqq%')
print s0.count_substrings(0) , 0
print s0.count_substrings(1) , 4
print s0.count_substrings(2) , 5
print s0.count_substrings(5) , 7
print s0.count_substrings(15) , 0
s4 = CombStr('29389efj s9fbsyaedg dBD QYDUEHWFUHB&*#(@)(#!')
print s4.count_substrings(1)
s1  = CombStr('')
print s1.count_substrings(0), 0
print s1.count_substrings(1), 0
s2  = CombStr('?')
print s2.count_substrings(0), 0
s5  = CombStr("A taste of honey. Tasting much sweeter than wine. I dream of your first kiss. And then I feel upon my lips again. A taste of honey. Tasting much sweeter than wine. I will return, yes I will return. I'll come back for the honey and you. Yours was the kiss that awoke my heart. There lingers still, though we're far apart. That taste of honey. Tasting much sweeter than wine. Oh I will return, yes I will return. I'll come back (He'll come back). for the honey (For the honey). and you")
print s5.count_substrings(7)
