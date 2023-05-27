import random
import MyPoint3d as mp3
import MyLine3d as ml3


def change_coordinate_fix(fix, fix_x, fix_y, fix_z, point):
    if fix == 0:
        point.x = fix_x
    elif fix == 1:
        point.y = fix_y
    else:
        point.z = fix_z


class MyFace3d:
    def __init__(self, contour=[], lines=[], points=[]):
        self.__points = []
        self.__lines = []
        self.__contour = []
        if contour == []:
            self.set_random_face()
        else:
            self.__contour = contour
            self.__lines = lines
            self.__points = points

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points):
        self.__points = points

    @property
    def contour(self):
        return self.__contour

    @contour.setter
    def contour(self, contour):
        self.__contour = contour

    @property
    def lines(self):
        return self.__contour

    @lines.setter
    def lines(self, lines):
        self.__lines = lines

    def set_random_face(self):
        self.__contour = []
        self.__lines = []
        self.__points = []
        count = random.randint(3, 6)
        # Переписать метод. Генерировать точки. Сортировать по координатам.
        # Выстраивать линии на основе точек. Проверка на выпуклость.
        fix = random.randint(0, 2)
        fix_x = fix_y = fix_z = None
        list_lines_contour = [ml3.MyLine3d()]
        if fix == 0:
            fix_x = list_lines_contour[0].point2.x = list_lines_contour[0].point1.x
        elif fix == 1:
            fix_y = list_lines_contour[0].point2.y = list_lines_contour[0].point1.y
        else:
            fix_z = list_lines_contour[0].point2.z = list_lines_contour[0].point1.z
        for i in range(1, count):
            tp1 = list_lines_contour[i - 1].point2
            tp2 = mp3.MyPoint3d()
            change_coordinate_fix(fix, fix_x, fix_y, fix_z, tp2)
            tl = ml3.MyLine3d(tp1, tp2)
            list_lines_contour.append(tl)
        list_lines_contour[count - 1].point2 = list_lines_contour[0].point1
        self.__contour = list_lines_contour
        self.__lines = self.__contour
        for i in range(count):
            self.__points.append(list_lines_contour[i].point1)


