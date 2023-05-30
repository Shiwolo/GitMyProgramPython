class Shape():
    def __init__(self, area, Perimeter):
        self.area = area
        self.Perimeter = Perimeter

    def getArea(self):
        return self.area

    def getPerimeter(self):
        return self.Perimeter


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getArea(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def getPerimeter(self):
        return self.a + self.b + self.c


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return 3.14 * self.radius ** 2

    def getPerimeter(self):
        return 2 * 3.14 * self.radius


t = Triangle(6, 6, 6)
print("三角形面积：", t.getArea())
print("三角形周长：", t.getPerimeter())

r = Rectangle(9, 5)
print("直角三角形面积：", r.getArea())
print("直角三角形周长：", r.getPerimeter())

c = Circle(10)
print("圆形面积：", c.getArea())
print("圆形周长：", c.getPerimeter())
