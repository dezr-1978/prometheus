'''
��������� ������� bouquets(narcissus_price, tulip_price, rose_price, summ), 
��� ������ 4 ��������� -- ������ ���� ����� (���� �� ���� ������, ������� �� �������, � ���� ������ � ����� ��������� �����), 
�� ������� ���� ����� -- ������� ������� ������, �� ����� ������� � ��� ���� ����, ����� ��� ������� ������� ������ �� ������������ summ.
�� ������, �� ������ � ������ (���������) ������� ���� ����� ������� �� �������. ����� �� ������������ ������ �� �����������.
������� ����������� �� ��� ����������:
print bouquets(1,1,1,5) # 34
print bouquets(2,3,4,10) # 12
print bouquets(2,3,4,100) # 4019
print bouquets(200,300,400,10000) # 4019
print bouquets(200,300,400,100000) # 3524556
'''


def bouquets(narcissus_price, tulip_price, rose_price, summ):
    	counter = 0
    	prices=sorted([narcissus_price, tulip_price,rose_price])

    	maximum_quantity = int(round(summ / prices[0]))
    	midlle_quantity = int(round(summ/ prices[1]))
    	minimum_quantity = int(round(summ/ prices[2]))

    	for i in range(maximum_quantity+1):
    		if i*prices[0] <= summ:
    			for j in range(midlle_quantity+1):
    				if j*prices[1]+i*prices[0] <= summ:
    					for k in range(minimum_quantity+1):
    						if (i*prices[0]+j*prices[1]+k*prices[2])<=summ and (i+j+k)%2!=0:
    							counter += 1

    	return counter



print bouquets(1,1,1,5) # 34
print bouquets(2,3,4,10) # 12
print bouquets(2,3,4,100) # 4019
print bouquets(200,300,400,10000) # 4019
print bouquets(200,300,400,100000) # 3524556
