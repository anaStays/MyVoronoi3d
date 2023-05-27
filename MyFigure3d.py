import MyPoint3d as mp3
import MyLine3d as ml3
import MyFace3d as mf3


class MyFigure3d:
    def __init__(self, list_faces: mf3.MyFace3d = []):
        self.faces = list_faces
