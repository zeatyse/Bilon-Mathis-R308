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


class Cercle:

    def __init__(self, rayon, centre=None):
        self.__rayon = float(rayon)

        if centre is None:
            self.__centre = Point()
        else:
            self.__centre = centre

    @property
    def rayon(self):
        return self.__rayon

    @rayon.setter
    def rayon(self, rayon):
        self.__rayon = float(rayon)

    @property
    def centre(self):
        return self.__centre

    @centre.setter
    def centre(self, centre):
        self.__centre = centre

    def diametre(self) -> float:
        return 2 * self.rayon

    def perimetre(self) -> float:
        return 2 * math.pi * self.rayon

    def surface(self) -> float:
        return math.pi * self.rayon ** 2

    def intersection(self, autre: "Cercle") -> bool:
        distance = self.centre.distancePoint(autre.centre)
        return distance <= self.rayon + autre.rayon

    def appartient(self, point: Point) -> bool:
        distance = self.centre.distancePoint(point)
        return distance <= self.rayon


def main():

    p1 = Point()
    p2 = Point(3, 4)

    print(p1.x, p1.y)
    print(p2.x, p2.y)

    print(p1.distanceCoord(3, 4))
    print(p1.distancePoint(p2))

    cercle1 = Cercle(5)

    print("\nCercle 1")
    print("Centre :", cercle1.centre.x, cercle1.centre.y)
    print("Rayon :", cercle1.rayon)
    print("Diamètre :", cercle1.diametre())
    print("Périmètre :", cercle1.perimetre())
    print("Surface :", cercle1.surface())

    centre2 = Point(3, 4)
    cercle2 = Cercle(2, centre2)

    print("\nCercle 2")
    print("Centre :", cercle2.centre.x, cercle2.centre.y)
    print("Rayon :", cercle2.rayon)

    print("\nIntersection :", cercle1.intersection(cercle2))

    p3 = Point(3, 0)

    print("Le point (3, 0) appartient au cercle 1 :", cercle1.appartient(p3))


if __name__ == "__main__":
    main()