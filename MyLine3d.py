import MyPoint3d as mp3


def generate_random_lines(n: int):
    lines = []
    for i in range(n):
        lines.append(MyLine3d())
    return lines


def get_list_line_x(line):
    list_x = [line.point1.x, line.point2.x]
    return list_x


def get_list_line_y(line):
    list_y = [line.point1.y, line.point2.y]
    return list_y


def get_list_line_z(line):
    list_z = [line.point1.z, line.point2.z]
    return list_z


def get_coordinates_line_xyz(line):
    return get_list_line_x(line), get_list_line_y(line), get_list_line_z(line)


class MyLine3d:
    def __init__(self, point1: mp3.MyPoint3d = None, point2: mp3.MyPoint3d = None):
        # self.__point1 = None
        # self.__point2 = None
        if point1 is None and point2 is None:
            self.set_random_line()
        else:
            self.__point1 = point1
            self.__point2 = point2

    # def get_point1(self):
    #     return self.point1
    #
    # def set_point1(self, point1):
    #     self.point1 = point1
    #
    # def get_point2(self):
    #     return self.point2
    #
    # def set_point2(self, point2):
    #     self.point2 = point2
    def __repr__(self):
        print(f"point1 = {self.point1.x}, {self.point1.y}, {self.point1.z}")
        print(f"point2 = {self.point2.x}, {self.point2.y}, {self.point2.z}")
        return ''

    @property
    def point1(self):
        return self.__point1

    @point1.setter
    def point1(self, point1):
        self.__point1 = point1

    @property
    def point2(self):
        return self.__point2

    @point2.setter
    def point2(self, point2):
        self.__point2 = point2

    def set_random_line(self):
        self.__point1 = mp3.MyPoint3d()
        self.__point2 = mp3.MyPoint3d()

