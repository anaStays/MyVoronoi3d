import MyPoint3d as mp3
import MyLine3d as ml3
import MyFace3d as mf3
import FunctionsForVoronoi as ffv

def get_static_cube():
    list_floats = [
        -0.500000, 0.500000, 0.500000,  # 0
        -0.500000, -0.500000, 0.500000,  # 1
        -0.500000, 0.500000, -0.500000,  # 2
        -0.500000, -0.500000, -0.500000,  # 3
        0.500000, 0.500000, 0.500000,  # 4
        0.500000, -0.500000, 0.500000,  # 5
        0.500000, 0.500000, -0.500000,  # 6
        0.500000, -0.500000, -0.500000  # 7
    ]
    lp = mf3.get_list_points_from_list_floats(list_floats)
    list_indexes = [
        [3, 2, 6, 7],
        [3, 2, 0, 1],
        [3, 1, 5, 7],
        [2, 0, 4, 6],
        [6, 7, 5, 4],
        [5, 4, 0, 1]
    ]
    list_faces = mf3.get_faces_from_list_points_and_indexes(lp, list_indexes)
    for i in range(len(list_faces)):
        list_faces[i].points = mf3.get_points_for_diagram_square(list_faces[i], 5)
    # list_faces[0].points = mf3.get_points_for_diagram_square(list_faces[0], 5)
    return list_faces


def get_diagram_for_figure(figure):
    list_voronoi_lines = []
    for i in range(len(figure.faces)):
        list_voronoi_lines.append(ffv.get_Voronoi_diagram_for_face(figure.faces[i]))
    return list_voronoi_lines


class MyFigure3d:
    def __init__(self, list_faces: mf3.MyFace3d = []):
        if list_faces == []:
            self.__faces = get_static_cube()
        else:
            self.__faces = list_faces

    @property
    def faces(self):
        return self.__faces

    @faces.setter
    def points(self, faces):
        self.__faces = faces
