import MyPoint3d as mp3
import MyLine3d as ml3
import random
import MyFace3d as mf3
import MyFigure3d as mfg3


def get_intersection_point(line1, line2, fix):
    if fix == 0:
        a1 = line1.point1.z - line1.point2.z
        b1 = line1.point2.y - line1.point1.y
        c1 = line1.point1.y * line1.point2.z - line1.point2.y * line1.point1.z
        a2 = line2.point1.z - line2.point2.z
        b2 = line2.point2.y - line2.point1.y
        c2 = line2.point1.y * line2.point2.z - line2.point2.y * line2.point1.z
    elif fix == 1:
        a1 = line1.point1.z - line1.point2.z
        b1 = line1.point2.x - line1.point1.x
        c1 = line1.point1.x * line1.point2.z - line1.point2.x * line1.point1.z
        a2 = line2.point1.z - line2.point2.z
        b2 = line2.point2.x - line2.point1.x
        c2 = line2.point1.x * line2.point2.z - line2.point2.x * line2.point1.z
    else:
        a1 = line1.point1.y - line1.point2.y
        b1 = line1.point2.x - line1.point1.x
        c1 = line1.point1.x * line1.point2.y - line1.point2.x * line1.point1.y
        a2 = line2.point1.y - line2.point2.y
        b2 = line2.point2.x - line2.point1.x
        c2 = line2.point1.x * line2.point2.y - line2.point2.x * line2.point1.y
    det = a1 * b2 - a2 * b1
    coordinate1 = (b1 * c2 - b2 * c1) / det
    coordinate2 = (a2 * c1 - a1 * c2) / det
    if fix == 0:
        intersection_point = mp3.MyPoint3d(line1.point1.x, coordinate1, coordinate2)
    elif fix == 1:
        intersection_point = mp3.MyPoint3d(coordinate1, line1.point1.y, coordinate2)
    else:
        intersection_point = mp3.MyPoint3d(coordinate1, coordinate2, line1.point1.z)
    print(intersection_point)
    return intersection_point


def is_point_inside_face(face, point):
    xmin, xmax = mf3.get_min_max_x(face)
    ymin, ymax = mf3.get_min_max_y(face)
    zmin, zmax = mf3.get_min_max_z(face)
    flag = 0
    if xmin <= point.x <= xmax and ymin <= point.y <= ymax and zmin <= point.z <= zmax:
        flag = 1
    return flag


def get_median_perpendicular(face, point1, point2):
    line = ml3.MyLine3d(point1, point2)
    point3 = point1
    perpendicular = ml3.MyLine3d()
    fix = mf3.find_fix(face)
    midpoint = find_midpoint(point1, point2, fix)
    if fix == 0:
        if (line.point2.z - line.point1.z) == 0:
            zmin, zmax = mf3.get_min_max_z(face)
            perpendicular.point1 = mp3.MyPoint3d(line.point1.x, midpoint.y, zmin)
            perpendicular.point2 = mp3.MyPoint3d(line.point1.x, midpoint.y, zmax)
        elif (line.point2.y - line.point1.y) == 0:
            ymin, ymax = mf3.get_min_max_y(face)
            perpendicular.point1 = mp3.MyPoint3d(line.point1.x, ymin, midpoint.z)
            perpendicular.point2 = mp3.MyPoint3d(line.point1.x, ymax, midpoint.z)
        else:
            k = (point2.z - point1.z) / (point2.y - point1.y)  # Угловой коэффициент
            b = (point2.y * point1.z - point1.y * point2.z) / (point2.y - point1.y)  # Смещение прямой
            d = midpoint.z + ((1 / k) * midpoint.y)  # Из теоремы о перпендикулярных прямых
            perpendicular.point1.y, perpendicular.point2.y = mf3.get_min_max_y(face)
            perpendicular.point1.z = (-1.0 / k) * perpendicular.point1.y + d
            perpendicular.point2.z = (-1.0 / k) * perpendicular.point2.y + d
            perpendicular.point1.x = perpendicular.point2.x = point1.x
            final_perpendicular_points = []
    elif fix == 1:
        if (line.point2.z - line.point1.z) == 0:
            zmin, zmax = mf3.get_min_max_z(face)
            perpendicular.point1 = mp3.MyPoint3d(midpoint.x, line.point1.y, zmin)
            perpendicular.point2 = mp3.MyPoint3d(midpoint.x, line.point1.y, zmax)
        elif (line.point2.x - line.point1.x) == 0:
            xmin, xmax = mf3.get_min_max_x(face)
            perpendicular.point1 = mp3.MyPoint3d(xmin, line.point1.y, midpoint.z)
            perpendicular.point2 = mp3.MyPoint3d(xmax, line.point1.y, midpoint.z)
        else:
            k = (point2.z - point1.z) / (point2.x - point1.x)  # Угловой коэффициент
            b = (point2.x * point1.z - point1.x * point2.z) / (point2.x - point1.x)  # Смещение прямой
            d = midpoint.z + ((1 / k) * midpoint.x)  # Из теоремы о перпендикулярных прямых
            perpendicular.point1.x, perpendicular.point2.x = mf3.get_min_max_x(face)
            perpendicular.point1.z = (-1.0 / k) * perpendicular.point1.x + d
            perpendicular.point2.z = (-1.0 / k) * perpendicular.point2.x + d
            perpendicular.point1.y = perpendicular.point2.y = point1.y
            final_perpendicular_points = []
    else:
        if (line.point2.y - line.point1.y) == 0:
            ymin, ymax = mf3.get_min_max_y(face)
            perpendicular.point1 = mp3.MyPoint3d(midpoint.x, ymin, line.point1.z)
            perpendicular.point2 = mp3.MyPoint3d(midpoint.x, ymax, line.point1.z)
        elif (line.point2.x - line.point1.x) == 0:
            xmin, xmax = mf3.get_min_max_x(face)
            perpendicular.point1 = mp3.MyPoint3d(xmin, midpoint.y, line.point1.z)
            perpendicular.point2 = mp3.MyPoint3d(xmax, midpoint.y, line.point1.z)
        else:
            k = (point2.y - point1.y) / (point2.x - point1.x) # Угловой коэффициент
            b = (point2.x * point1.y - point1.x * point2.y) / (point2.x - point1.x) # Смещение прямой
            d = midpoint.y + ((1 / k) * midpoint.x) # Из теоремы о перпендикулярных прямых
            perpendicular.point1.x, perpendicular.point2.x = mf3.get_min_max_x(face)
            perpendicular.point1.y = (-1.0 / k) * perpendicular.point1.x + d
            perpendicular.point2.y = (-1.0 / k) * perpendicular.point2.x + d
            perpendicular.point1.z = perpendicular.point2.z = point1.z
            final_perpendicular_points = []
    for i in range(len(face.contour)):
        new_point = get_intersection_point(face.contour[i], perpendicular, fix)
        if is_point_inside_face(face, new_point):
            final_perpendicular_points.append(new_point)
    final_perpendicular = ml3.MyLine3d(final_perpendicular_points[0], final_perpendicular_points[1])
    return final_perpendicular


def find_midpoint(point1, point2, fix):
    x = (point1.x + point2.x) / 2
    y = (point1.y + point2.y) / 2
    z = (point1.z + point2.z) / 2
    if fix == 0:
        midpoint = mp3.MyPoint3d(point1.x, y, z)
    elif fix == 1:
        midpoint = mp3.MyPoint3d(x, point1.y, z)
    else:
        midpoint = mp3.MyPoint3d(x, y, point1.z)
    return midpoint


# def find_perpendicular(face, line):
#     fix = mf3.find_fix(face)
#     midpoint = find_midpoint(line.point1, line.point2, fix)
#     # Вычисление углового коэффициента перпендикулярной прямой
#     if fix == 0:
#     elif fix == 1:
#     else:
#         if (line.point2.y - line.point1.y) == 0:
#             ymin, ymax = mf3.get_min_max_y(face)
#             perpendicular_point1 = mp3.MyPoint3d(midpoint.x, ymin, line.point1.z)
#             perpendicular_point2 = mp3.MyPoint3d(midpoint.x, ymax, line.point1.z)
#         elif (line.point2.x - line.point1.x) == 0:
#             xmin, xmax = mf3.get_min_max_x(face)
#             perpendicular_point1 = mp3.MyPoint3d(xmin, midpoint.y, line.point1.z)
#             perpendicular_point2 = mp3.MyPoint3d(xmax, midpoint.y, line.point1.z)
#         else:
#             xmin, xmax = mf3.get_min_max_x(face)
#             slope = (line.point2.y - line.point1.y) / (line.point2.x - line.point1.x)
#             perpendicular_slope = -1 / slope
#             # Вычисление точки на перпендикулярной прямой
#             x = xmin  # Произвольное значение x на прямой
#             y = midpoint.y + perpendicular_slope  # Вычисление соответствующего y на перпендикулярной прямой
#
#     perpendicular_line = ml3.MyLine3d(perpendicular_point1, perpendicular_point2)
#     return perpendicular_line

