from board import XO_points, X_points, O_points
from logic import winning_possibilities

def auto_play():
    for wp in winning_possibilities:
        wp.check('O')
        if wp.p1_satisfied and wp.p2_satisfied:
            play_point(wp.x3, wp.y3)
            return
        elif wp.p2_satisfied and wp.p3_satisfied:
            play_point(wp.x1, wp.y1)
            return
        elif wp.p3_satisfied and wp.p1_satisfied:
            play_point(wp.x2, wp.y2)
            return

    for wp in winning_possibilities:
        wp.check('X')
        if wp.p1_satisfied and wp.p2_satisfied:
            play_point(wp.x3, wp.y3)
            return
        elif wp.p2_satisfied and wp.p3_satisfied:
            play_point(wp.x1, wp.y1)
            return
        elif wp.p3_satisfied and wp.p1_satisfied:
            play_point(wp.x2, wp.y2)
            return

    play_point(2, 2, force=True)
    corner_points = [(1,1),(1,3),(3,1),(3,3)]
    middle_points = [(1,2),(2,1),(2,3),(3,2)]
    num_corners = sum(1 for p in X_points if (p.x,p.y) in corner_points)

    if num_corners >= 2:
        for point in XO_points:
            if (point.x,point.y) in middle_points and point not in X_points + O_points:
                point.set()
                return
    else:
        for point in XO_points:
            if (point.x,point.y) in corner_points and point not in X_points + O_points:
                point.set()
                return

def play_point(x, y, force=False):
    for point in XO_points:
        if point.x == x and point.y == y and (force or point not in X_points + O_points):
            point.set()
            return
