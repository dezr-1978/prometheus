import math
'''
��������� ����� Sphere ��� ������������� ����� � ����������� �������.
����������� ������� ������ �����:
�����������, ���� ������ 4 ������ �����: �����, �� 3 ���������� ������ ���. ���� ����������� ����������� ��� ���������, �������� ��'��� ����� �� ��������� ������� �� ������� � ������� ���������. ���� ����������� ����������� � 1 ����������, �������� ��'��� ����� � ��������� ������� �� ������� � ������� ���������.
����� get_volume(), ���� ������� ����� ����� -- ��'�� ���, �������� �������� ������.
����� get_square(), ���� ������� ����� ����� -- ����� �������� ������� �����.
����� get_radius(), ���� ������� ����� ����� -- ����� �����.
����� get_center(), ���� ������� ����� �� 3 ������� ������� -- ������������ ������ ����� � ���� � �������, � ���� ���� ��������� � �����������.
����� set_radius(r), ���� ������ 1 �������� -- ����� �����, �� ����� ����� ������� �����, ����� �� ����������.
����� set_center(x,y,z), ���� ������ 3 ��������� -- ������ �����, �� ����� ���������� ������ �����, ����� �� ����������. ���������� ��������� � ���� � �������, �� � � �����������.
����� is_point_inside(x,y,z), ���� ������ 3 ��������� -- ������ ����� -- ���������� ����� ����� � ������� (� ���� � �������, �� � � �����������), �� ������� ������ �������� True ��� False � ��������� �� ����, �� ����������� �� ����� �������� �����.
����� �� ������������ ������ �� �����������.
������� ����������� �� ��� ���������� �����:
s0 = Sphere(0.5) # test sphere creation with radius and default center
print s0.get_center() # (0.0, 0.0, 0.0)
print s0.get_volume() # 0.523598775598
print s0.is_point_inside(0, -1.5, 0) # False
s0.set_radius(1.6) 
print s0.is_point_inside(0, -1.5, 0) # True
print s0.get_radius() # 1.6
'''

class Sphere(object):
    
    def __init__(self, radius = 1, x = 0, y = 0, z = 0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z
    
    def get_volume(self):
        return 4*math.pi*self.radius*self.radius*self.radius/3
    #(4.0 / 3.0) * (math.pi * (self.radius**3))
        
    def get_square(self):
        return 4.0 * math.pi * self.radius * self.radius
        
    def get_radius(self):
        return self.radius
        
    def get_center(self):
        return float(self.x), float(self.y), float(self.z)
            
    def set_radius(self, r):
        self.radius = r
        
    def set_center(self, x1, y1, z1):
            self.x = x1 
            self.y = y1 
            self.z = z1
        
    def is_point_inside(self, x, y, z):
        a = math.sqrt((self.x - x)**2 + (self.y - y)**2 + (self.z - z)**2)
        if a <= self.radius:
            return True
        else:
            return False

s1 = Sphere(0.5)

print s1.get_center(), '== (0, 0, 0)'
print s1.get_radius(), '== 1'
print s1.get_volume(), '== 4.18879020479'
print s1.get_square(), '== 12.5663706144'
print s1.is_point_inside(0, 0.99, 0), '== True'
print s1.is_point_inside(0.99, 0, 0), '== True'
print s1.is_point_inside(0, 0, 0.99), '== True'
s1.set_radius(1.1)
s1.set_center(0.5, 1, 0)
print s1.is_point_inside(0, 0.99, 0), '== True'
print s1.is_point_inside(0.99, 0, 0), '== False'
print s1.is_point_inside(0, 0, 0.99), '== False'
print s1.get_center(), '== (0.5, 1, 0)'
print s1.get_radius(), '== 1.1'
s2 = Sphere(2)
print s2.get_center(), '== (0, 0, 0)'
print s2.get_radius(), '== 2'
print s2.is_point_inside(0, 0.99, 0), '== True'
print s2.is_point_inside(1.99, 0, 0), '== True'
print s2.is_point_inside(0, 0, 2.99), '== False'
s3 = Sphere(1.99, 1, 2, -1)
print s3.get_center(), '== (1, 2, -1)'
print s3.get_radius(), '== 1.99'
print s3.is_point_inside(0, 0.99, 0), '== True'
print s3.is_point_inside(0.99, 0, 0), '== False'
print s3.is_point_inside(0, 0, 0.99), '== False'
