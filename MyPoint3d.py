import random


def generate_random_points(n: int):
    res = []
    for i in range(n):
        res.append(MyPoint3d())
    return res


def get_list_x(list_points):
    list_x=[]
    for i in range(len(list_points)):
        list_x.append(list_points[i].x)
    return list_x


def get_list_y(list_points):
    list_y=[]
    for i in range(len(list_points)):
        list_y.append(list_points[i].y)
    return list_y


def get_list_z(list_points):
    list_z=[]
    for i in range(len(list_points)):
        list_z.append(list_points[i].z)
    return list_z


def get_coordinates_points_xyz(list_points):
    return get_list_x(list_points), get_list_y(list_points), get_list_z(list_points)


class MyPoint3d:
    def __init__(self, x: float = None, y: float = None, z: float = None):
        if x == None and y == None and z == None:
            self.set_random_point()
        else:
            self.x = x
            self.y = y
            self.z = z

    def __repr__(self):
        print(f"{self.x}, {self.y}, {self.z}")

    def set_random_point(self):
        self.x = random.uniform(0, 2)
        self.y = random.uniform(0, 2)
        self.z = random.uniform(0, 2)

