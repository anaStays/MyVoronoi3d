import MyPoint3d as mp3
import MyLine3d as ml3
import random
import MyFace3d as mf3
import MyFigure3d as mfg3
import  MyPoint2d as mp2
from operator import attrgetter


def cmp(a, b):
    return a.x < b.x or (a.x == b.x and a.y < b.y)


def cw(a, b, c):
    return a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y) < 0


def ccw(a, b, c):
    return a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y) > 0


def get_convex_hull_2d(st_points):
    a = st_points[:]
    if len(a) != 1:
        a.sort(key=lambda p: (p.x, p.y))
        p1, p2 = a[0], a[-1]
        up, down = [p1], [p1]
        for i in range(1, len(a)):
            if i == len(a) - 1 or cw(p1, a[i], p2):
                while len(up) >= 2 and not cw(up[-2], up[-1], a[i]):
                    up.pop()
                up.append(a[i])
            if i == len(a) - 1 or ccw(p1, a[i], p2):
                while len(down) >= 2 and not ccw(down[-2], down[-1], a[i]):
                    down.pop()
                down.append(a[i])
        a.clear()
        for i in range(len(up)):
            a.append(up[i])
        for i in range(len(down) - 2, 0, -1):
            a.append(down[i])
    return a


def get_convex_hull_3d(points, fix):
    points_2d = []
    for i in range(len(points)):
        points_2d.append(mp2.converter_from3d_to2d(points[i], fix))
    res = get_convex_hull_2d(points_2d)
    res_3 = []
    for i in range (len(res)):
        res_3.append(mp2.converter_from2d_to3d(res[i], points[0], fix))
    return get_line_from_points(res_3)


def get_line_from_points(points):
    lines = []
    for i in range(len(points)-1):
        lines.append(ml3.MyLine3d(points[i], points[i+1]))
    lines.append(ml3.MyLine3d(points[-1], points[0]))
    return lines


def are_points_on_same_side(fix, line, point1, point2):
    if fix == 0:
        x1, y1 = line.point1.y, line.point1.z
        x2, y2 = line.point2.y, line.point2.z
        x0, y0 = point1.y, point1.z
        x3, y3 = point2.y, point2.z
    elif fix == 1:
        x1, y1 = line.point1.x, line.point1.z
        x2, y2 = line.point2.x, line.point2.z
        x0, y0 = point1.x, point1.z
        x3, y3 = point2.x, point2.z
    else:
        x1, y1 = line.point1.x, line.point1.y
        x2, y2 = line.point2.x, line.point2.y
        x0, y0 = point1.x, point1.y
        x3, y3 = point2.x, point2.y
    a = y2 - y1
    b = x1 - x2
    c = (x2 * y1) - (x1 * y2)
    value1 = (a * x0) + (b * y0) + c
    value2 = (a * x3) + (b * y3) + c
    if value1 * value2 >= 0 - 0.00001:
        return True  # Точки находятся по одну сторону от линии
    else:
        return False  # Точки находятся по разные стороны от линии


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
    # if det == 0:
    coordinate1 = (b1 * c2 - b2 * c1) / det
    coordinate2 = (a2 * c1 - a1 * c2) / det
    if fix == 0:
        intersection_point = mp3.MyPoint3d(line1.point1.x, coordinate1, coordinate2)
    elif fix == 1:
        intersection_point = mp3.MyPoint3d(coordinate1, line1.point1.y, coordinate2)
    else:
        intersection_point = mp3.MyPoint3d(coordinate1, coordinate2, line1.point1.z)
    # print(intersection_point)
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


def get_Voronoi_diagram_for_face(face):
    fix = mf3.find_fix(face)
    sort_list = sorted(face.points, key=attrgetter('x', 'y', 'z'))
    voronoi_lines = []
    for i in range(len(sort_list)):
        perp_list = []
        mb_voronoi_points = []
        del_points = []
        for j in range(len(face.contour)):
            mb_voronoi_points.append(face.contour[j].point1)
        #for j in range(i+1, len(sort_list)):
        for j in range(len(sort_list)):
            if i != j:
                perp = get_median_perpendicular(face, sort_list[i], sort_list[j])
                mb_voronoi_points.append(perp.point1)
                mb_voronoi_points.append(perp.point2)
                for k in range(len(perp_list)):
                    intersection_point = get_intersection_point(perp, perp_list[k], fix)
                    if is_point_inside_face(face, intersection_point):
                        mb_voronoi_points.append(intersection_point)
            # for k in range(len(voronoi_lines)):
            #     intersection_point = get_intersection_point(perp, voronoi_lines[k], fix)
            #     if is_point_inside_face(face, intersection_point):
            #         mb_voronoi_points.append(intersection_point)
            #         perp_list.append(voronoi_lines[k])
                perp_list.append(perp)
        for j in range(len(perp_list)):
            k = 0
            while k < len(mb_voronoi_points):
                if not are_points_on_same_side(fix, perp_list[j], sort_list[i], mb_voronoi_points[k]):
                    del_points.append(mb_voronoi_points[k])
                    mb_voronoi_points.pop(k)
                else:
                    k += 1
        voronoi_lines += get_convex_hull_3d(mb_voronoi_points, fix)
    face.lines = voronoi_lines
    return voronoi_lines




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

