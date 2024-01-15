import math

class Shape:

    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B

    def area(self):
        return '{} {}'.format(self.R, self.B)

    def ps_print(self):
        self.B = int(self.R * self.G)


class Circle(Shape):
    raise_amt = 1.10

    def __init__(self, R, G, B, x1, y1, radius):
        super().__init__(R, G, B)
        self.x1 = x1
        self.y1 = y1
        self.radius = radius
    def area(self):
        Area = math.pi*(self.radius**2)
        
        return Area
    def ps_print(self):
        print("Circle Area = ", self.radius)
    

class Trangle(Shape):
    raise_amt = 1.50

    def __init__(self, R, G, B, x1, y1, x2, y2, x3, y3):
        super().__init__(R, G, B)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def add_emp(self, x1):
        print("hello", self.x1)

    def area(self):
        print("world", self.x2)

    def ps_print(self):
        print("hello", self.x3)

if __name__ == '__main__':
    dev_1 = Circle(4,5,7,8,9,10)
    dev_2 = Circle(1, 10, 60, 20, 30,40)
    mgr_1 = Trangle(100,200 ,300, 300, 60000, 2000, 200, 100, 500)

    print(mgr_1.ps_print())
    print(mgr_1.y3)
    print('基本年収（$）：', mgr_1.x3)
    mgr_1.ps_print()
    print('年間の役職手当（$）：', mgr_1.B)

    print(dev_1.ps_print())
    print("Circel area = ", dev_1.area())
    mgr_1.area()

