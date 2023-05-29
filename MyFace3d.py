import random
from operator import attrgetter
import MyPoint3d as mp3
import MyLine3d as ml3
import numpy as np


def change_coordinate_fix(fix, fix_x, fix_y, fix_z, point):
    if fix == 0:
        point.x = fix_x
    elif fix == 1:
        point.y = fix_y
    else:
        point.z = fix_z


def get_list_points_from_list_floats(list_floats):
    list_points = []
    for i in range(0, len(list_floats), 3):
        list_points.append(mp3.MyPoint3d(list_floats[i], list_floats[i + 1], list_floats[i + 2]))
    return list_points


def get_list_contour_from_list_points(list_points):
    contour = []
    for i in range(len(list_points) - 1):
        contour.append(ml3.MyLine3d(list_points[i], list_points[i + 1]))
    contour.append(ml3.MyLine3d(list_points[len(list_points) - 1], list_points[0]))
    return contour


def get_vector(point1, point2):
    return mp3.MyPoint3d(point2.x - point1.x, point2.y - point1.y, point2.z - point1.z)


def vector_product(point1, point2, point3):
    a = get_vector(point1, point2)
    b = get_vector(point2, point3)
    return mp3.MyPoint3d(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)


def vector_product_2d(point1, point2, point3, fix):
    a = get_vector(point1, point2)
    b = get_vector(point2, point3)
    a1 = [a.x, a.y, a.z]
    b1 = [b.x, b.y, b.z]
    if fix == 0:
        a1.pop(0)
        b1.pop(0)
    elif fix == 1:
        a1.pop(1)
        b1.pop(1)
    else:
        a1.pop(2)
        b1.pop(2)
    return np.cross(a1, b1)


def generate_list_points(first_point, count, fix, fix_x, fix_y, fix_z):
    new_list = [first_point]
    for i in range(1, count):
        tp = mp3.MyPoint3d()
        change_coordinate_fix(fix, fix_x, fix_y, fix_z, tp)
        new_list.append(tp)
    new_list = sorted(new_list, key=attrgetter('x', 'y', 'z'))
    # new_list.sort(key=lambda point: point.x)
    # print(new_list)
    return new_list


def is_face_convex(list_points, fix):
    flag = 1
    count = len(list_points)
    for i in range(2, count):
        if vector_product_2d(list_points[i - 2], list_points[i - 1], list_points[i], fix) >= 0:
            flag = 0
    if vector_product_2d(list_points[count - 2], list_points[count - 1], list_points[0], fix) >= 0:
        flag = 0
    if vector_product_2d(list_points[count - 1], list_points[0], list_points[1], fix) >= 0:
        flag = 0
    return flag


# Метод получения граней через список точек и индексов граней
def get_faces_from_list_points_and_indexes(list_points, list_indexes):
    list_faces = []
    n = len(list_indexes)
    for i in range(n):
        contour = []
        points = []
        m = len(list_indexes[i])
        for j in range(m):
            points.append(list_points[list_indexes[i][j]])
            if j < m - 1:
                contour.append(ml3.MyLine3d(list_points[list_indexes[i][j]], list_points[list_indexes[i][j + 1]]))
        contour.append(ml3.MyLine3d(list_points[list_indexes[i][m - 1]], list_points[list_indexes[i][0]]))
        list_faces.append(MyFace3d(contour, contour, points))
    return list_faces


def get_points_for_diagram_square(face, count):
    list_points = []
    p1 = face.lines[0].point1
    p3 = face.lines[1].point2
    for i in range(count):
        x = random.uniform(p1.x, p3.x)
        y = random.uniform(p1.y, p3.y)
        z = random.uniform(p1.z, p3.z)
        print(x, y, z)
        list_points.append(mp3.MyPoint3d(x, y, z))
    print(list_points)
    return list_points


# Хранить список смежных граней, пригодится при рандомной генерации фигур
class MyFace3d:
    def __init__(self, contour=[], lines=[], points=[]):
        self.__points = []
        self.__lines = []
        self.__contour = []
        if contour == []:
            self.set_random_face_use_generate_points()
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

    def set_random_face_use_generate_lines(self, count=-1):
        self.__contour = []
        self.__lines = []
        self.__points = []
        if count == -1:
            count = random.randint(3, 6)
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

    def set_random_face_use_generate_points(self, count=-1):
        self.__contour = []
        self.__lines = []
        self.__points = []
        if count == -1 or count < 3:
            count = random.randint(3, 6)
        fix = random.randint(0, 2)
        fix_x = fix_y = fix_z = None
        first_point = mp3.MyPoint3d()
        if fix == 0:
            fix_x = first_point.x
        elif fix == 1:
            fix_y = first_point.y
        else:
            fix_z = first_point.z
        flag = 0
        while not flag:
            list_points = generate_list_points(first_point, count, fix, fix_x, fix_y, fix_z)
            flag = is_face_convex(list_points, fix)
        for i in range(0, count - 1):
            self.__contour.append(ml3.MyLine3d(list_points[i], list_points[i + 1]))
        self.__contour.append(ml3.MyLine3d(list_points[count - 1], list_points[0]))
        self.__lines = self.__contour
        self.__points = list_points
