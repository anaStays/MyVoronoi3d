import random
import MyPoint3d as mp3
import MyLine3d as ml3


class MyFace3d:
    def __init__(self, contour, lines, points):
        self.contour = contour
        self.lines = lines
        self.points = points

    def __init__(self):
        self.points = []
        self. lines = []
        self. contour = []
        self.set_random_face()

    def set_random_face(self):
        count = random.randint(3, 6)
        list_lines_contour = []
        line = ml3.MyLine3d()
        list_lines_contour.append(ml3.MyLine3d())
        for i in range(1, count):
            tp1 = ml3.MyLine3d(list_lines_contour[i-1].point2)
            tp2 = mp3.MyPoint3d()
            tl = ml3.MyLine3d(tp1, tp2)
            list_lines_contour.append(tl)
        self.contour = list_lines_contour
        for i in range(count):
            self.points.append(list_lines_contour[i].point1)
            self.lines.append(list_lines_contour[i])
