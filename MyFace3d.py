import random
import MyPoint3d as mp3
import MyLine3d as ml3


class MyFace3d:
    def __init__(self, contour = [], lines = [], points = []):
        self.points = []
        self.lines = []
        self.contour = []
        if contour == []:
            self.set_random_face()
        else:
            self.contour = contour
            self.lines = lines
            self.points = points


    def set_random_face(self):
        self.contour = []
        self.lines = []
        self.points = []
        count = random.randint(3, 6)
        fix = random.randint(0, 2)
        list_lines_contour = [ml3.MyLine3d()]
        for i in range(1, count):
            tp1 = list_lines_contour[i-1].point2
            tp2 = mp3.MyPoint3d()
            tl = ml3.MyLine3d(tp1, tp2)
            list_lines_contour.append(tl)
        list_lines_contour[count-1].point2 = list_lines_contour[0].point1
        self.contour = list_lines_contour
        self.lines = self.contour
        for i in range(count):
            self.points.append(list_lines_contour[i].point1)


