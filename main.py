import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.gridspec import GridSpec
import MyPoint3d as mp3
import MyLine3d as ml3
import random
import MyFace3d as mf3

def get_random_color():
    c = random.randint(100,999)
    return '#' + str(c)


def draw_line(line, my_color):
    if my_color=='-1':
        my_color = get_random_color()
    x, y, z = ml3.get_coordinates_line_xyz(line)
    ax_3d.plot(x, y, z, color = my_color)
    ax_3d.scatter(x, y, z, color = my_color)


def draw_lines(list_lines, my_color='-1'):
    for i in range(len(list_lines)):
        draw_line(list_lines[i], my_color)


def draw_points(list_points, my_color='-1'):
    if my_color == '-1':
        my_color = get_random_color()
    x, y, z = mp3.get_coordinates_points_xyz(list_points)
    ax_3d.scatter(x, y, z, color=my_color)


fig = plt.figure(figsize=(11, 6))
gs = GridSpec(ncols=11, nrows=6, figure=fig)
ax_3d = fig.add_subplot(gs[0:6,0:5], projection='3d')
ax_3d2 = fig.add_subplot(gs[0:6,6:], projection='3d')
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')
ax_3d2.set_xlabel('x')
ax_3d2.set_ylabel('y')
ax_3d2.set_zlabel('z')

if __name__ == '__main__':
    n = 5
    list_points = mp3.generate_random_points(n)
    # face = mf3.MyFace3d()
    # face.set_random_face()
    # draw_points(face.points)
    # draw_lines(face.contour)
    # draw_lines(face.lines)
    draw_points(list_points)

    plt.show()