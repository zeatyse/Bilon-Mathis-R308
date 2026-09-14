import math

class Point:

    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def distanceCoord(self, a: float, b: float) -> float:
        return math.sqrt((a - self.x) ** 2 + (b - self.y) ** 2)

    def distancePoint(self, camarade: "Point") -> float:
        return self.distanceCoord(camarade.x, camarade.y)
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = float(x)
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y = float(y)


p1 = Point()
p2 = Point(3, 4)

print(p1.x, p1.y)
print(p2.x, p2.y)

print(p1.distanceCoord(3, 4))
print(p1.distancePoint(p2))