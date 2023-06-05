import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.gridspec import GridSpec
import MyPoint3d as mp3
import MyLine3d as ml3
import random
import MyFace3d as mf3
import MyFigure3d as mfg3
import FunctionsForVoronoi as ffv


def get_random_color():
    return random.choice(colors)


def draw_line(line, ax, my_color='-1'):
    if my_color == '-1':
        my_color = get_random_color()
    x, y, z = ml3.get_coordinates_line_xyz(line)
    ax.plot(x, y, z, color=my_color)
    ax.scatter(x, y, z, color=my_color)


def draw_lines(list_lines, ax, my_color='-1'):
    if my_color == '-1':
        my_color = get_random_color()
    for i in range(len(list_lines)):
        draw_line(list_lines[i], ax, my_color)


def draw_points(list_points, ax, my_color='-1'):
    if my_color == '-1':
        my_color = get_random_color()
    x, y, z = mp3.get_coordinates_points_xyz(list_points)
    ax.scatter(x, y, z, color=my_color)


def draw_face(face, ax, my_color='-1'):
    if my_color == '-1':
        my_color = get_random_color()
    draw_points(face.points, ax, my_color)
    draw_lines(face.contour, ax, my_color)
    draw_lines(face.lines, ax, my_color)


def draw_figure(figure, ax, my_color='-1'):
    for i in range(len(figure.faces)):
        draw_face(figure.faces[i], ax, my_color)


# def draw_figures(figure1, figure2, ax1, ax2, my_color='-1'):
#     for i in range(len(figure1.faces)):
#         # if my_color == '-1':
#         #     my_color = get_random_color()
#         my_color = get_random_color()
#         draw_face(figure1.faces[i], ax1, my_color)
#         draw_face(figure2.faces[i], ax2, my_color)


def draw_figures(list_figures, list_axes, my_color='-1'):
    for i in range(len(list_figures[0].faces)):
        # if my_color == '-1':
        #     my_color = get_random_color()
        my_color = get_random_color()
        for j in range(len(list_figures)):
            draw_face(list_figures[j].faces[i], list_axes[j], my_color)

colors = ['#3a07c5', '#fa66ba', '#f94e50', '#fed3f2', '#edd8fe', '#dde2fe', '#6670fa', '#a14ef9', '#4ef9a1', '#f9f74e',
          '#9efc9d', '#fccb9d', '#fc9d9e', '#f8174c', '#3a80f9', '#f3cafd', '#f84586', '#3bf8b7']
fig = plt.figure(figsize=(11, 6))
gs = GridSpec(ncols=11, nrows=6, figure=fig)
ax_3d = fig.add_subplot(gs[0:6, 0:5], projection='3d')
ax_3d2 = fig.add_subplot(gs[0:6, 6:], projection='3d')
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')
ax_3d2.set_xlabel('x')
ax_3d2.set_ylabel('y')
ax_3d2.set_zlabel('z')


def test_perp():
    fig = mfg3.MyFigure3d()
    face = fig.faces[2]
    draw_face(face)
    new_list_points = [face.points[0], face.points[1], face.points[2], face.points[3]]
    fix = mf3.find_fix(face)
    # mf3.change_coordinate_fix(fix, face.contour[0].point1.x, face.contour[0].point1.y, face.contour[0].point1.z,
    #                           new_list_points[0])
    # mf3.change_coordinate_fix(fix, face.contour[0].point1.x, face.contour[0].point1.y, face.contour[0].point1.z,
    #                           new_list_points[1])
    line = ml3.MyLine3d(new_list_points[0], new_list_points[1])
    draw_line(line, '#F82E5D')
    lp = ffv.get_median_perpendicular(face, new_list_points[0], new_list_points[1])
    draw_line(lp, '#642EF8')


def test_mb_voronoi_points():
    fig = mfg3.MyFigure3d()
    face = fig.faces[1]
    draw_face(face, '#00FF02')
    fix = mf3.find_fix(face)
    ln = ffv.get_Voronoi_diagram_for_face(face)
    # draw_points(ps, '#004AFF')
    # draw_points(ds, '#FF00B0')
    draw_lines(ln)


def test_voronoi():
    fig = mfg3.MyFigure3d()
    fig1 = mfg3.MyFigure3d()
    # draw_figure(fig1, ax_3d)
    mfg3.get_diagram_for_figure(fig)
    # print(fig.faces[0].lines)
    # for i in range(len(list)):
    #     draw_lines(list[i])
    # draw_figure(fig, ax_3d2)
    draw_figures([fig, fig1], [ax_3d2, ax_3d])


if __name__ == '__main__':
    test_voronoi()
    # n = 5
    # list_points = mp3.generate_random_points(n)
    # fig = mfg3.MyFigure3d()
    # face = fig.faces[0]
    # draw_face(face)
    # fig = mfg3.MyFigure3d()
    # for i in range(5):
    #     mf3.change_coordinate_fix(0, 1, None, None, list_points[i])
    # line1 = ml3.MyLine3d(list_points[0], list_points[1])
    # line2 = ml3.MyLine3d(list_points[2], list_points[3])
    # p1 = ffv.get_intersection_point(line1, line2, 0)
    # p1 = ffv.find_intersection_point(line1, line2)
    # draw_lines([line1])
    # l1 = ml3.MyLine3d(mp3.MyPoint3d(1, 2, 0), mp3.MyPoint3d(4, 5, 0))
    # l2 = ml3.MyLine3d(mp3.MyPoint3d(3.5, 2.5, 0), mp3.MyPoint3d(2.5, 3.5, 0))
    # draw_lines([l1, l2])

    # draw_face(fig.faces[0])
    # p1 = fig.faces[0].contour[0].point1
    # p2 = fig.faces[0].contour[0].point2
    # p3 = fig.faces[0].contour[1].point2
    # fix = mp3.find_fix(p1, p2, p3)
    # perp = ffv.get_median_perpendicular(fig.faces[0], p1, p2, fix)
    # draw_lines([perp])

    # face = mf3.MyFace3d()
    # draw_points(face.points)
    # draw_lines(face.contour)
    # draw_lines(face.lines)
    # cube = mfg3.MyFigure3d()
    # for i in range(len(cube.faces)):
    #     draw_face(cube.faces[i])
    # print(lp)
    # print(list_floats)
    # lc = mf3.get_list_contour_from_list_points(lp)
    # draw_points(lp)
    # draw_lines(lc)
    # line = ml3.MyLine3d(list_points[0], list_points[1])
    plt.show()
