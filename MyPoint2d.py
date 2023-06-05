import random
import MyPoint3d as mp3


def converter_from3d_to2d(point3d, fix):
    if fix == 0:
        point2d = MyPoint2d(point3d.y, point3d.z)
    elif fix == 1:
        point2d = MyPoint2d(point3d.x, point3d.z)
    else:
        point2d = MyPoint2d(point3d.x, point3d.y)
    return point2d


def converter_from2d_to3d(point2d, point3d, fix):
    if fix == 0:
        point3d = mp3.MyPoint3d(point3d.x, point2d.x, point2d.y)
    elif fix == 1:
        point3d = mp3.MyPoint3d(point2d.x, point3d.y, point2d.y)
    else:
        point3d = mp3.MyPoint3d(point2d.x, point2d.y, point3d.z)
    return point3d


class MyPoint2d:
    def __init__(self, x: float = None, y: float = None):
        if x == None and y == None:
            self.set_random_point()
        else:
            self.__x = x
            self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def __repr__(self):
        print(f"{self.__x}, {self.__y}")
        return ''

    def set_random_point(self):
        self.__x = random.uniform(0, 2)
        self.__y = random.uniform(0, 2)

