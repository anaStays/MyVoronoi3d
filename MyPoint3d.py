import random


def find_fix(point1, point2, point3):
    if point1.x == point2.x == point3.x:
        fix = 0
    elif point1.y == point2.y == point3.y:
        fix = 1
    else:
        fix = 2
    return fix


def generate_random_points(n: int):
    res = []
    for i in range(n):
        res.append(MyPoint3d())
    return res


def get_list_points_x(list_points):
    list_x = []
    for i in range(len(list_points)):
        list_x.append(list_points[i].x)
    return list_x


def get_list_points_y(list_points):
    list_y = []
    for i in range(len(list_points)):
        list_y.append(list_points[i].y)
    return list_y


def get_list_points_z(list_points):
    list_z = []
    for i in range(len(list_points)):
        list_z.append(list_points[i].z)
    return list_z


def get_coordinates_points_xyz(list_points):
    return get_list_points_x(list_points), get_list_points_y(list_points), get_list_points_z(list_points)


class MyPoint3d:
    def __init__(self, x: float = None, y: float = None, z: float = None):
        if x == None and y == None and z == None:
            self.set_random_point()
        else:
            self.__x = x
            self.__y = y
            self.__z = z

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

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, z):
        self.__z = z

    def __repr__(self):
        print(f"{self.__x}, {self.__y}, {self.__z}")
        return ''



    def set_random_point(self):
        self.__x = random.uniform(0, 2)
        self.__y = random.uniform(0, 2)
        self.__z = random.uniform(0, 2)

