"""
Write a program to animate a face bouncing around a window. 
Use a list of graphics objects to represent the face.
"""

from graphics import GraphWin, Circle, Point, Polygon, Oval, update


def calculate_nose(center_point):
    nose_p1_x = center_point.getX() - 2
    nose_p1_y = center_point.getY() - 2
    nose_p2_x = center_point.getX() + 2
    nose_p2_y = center_point.getY() - 2
    nose_p3_x = center_point.getX()
    nose_p3_y = center_point.getY() + 2
    return Polygon(Point(nose_p1_x, nose_p1_y),
                   Point(nose_p2_x, nose_p2_y),
                   Point(nose_p3_x, nose_p3_y)
                   )


def calculate_mouth(center_point):
    mouth_p1_x = center_point.getX() - 4
    mouth_p1_y = center_point.getY() - 4
    mouth_p2_x = center_point.getX() + 4
    mouth_p2_y = center_point.getY() - 6   
    return Oval(Point(mouth_p1_x, mouth_p1_y),
                 Point(mouth_p2_x, mouth_p2_y)
                 )

def calculate_eyes(center_point):
    p1_x = center_point.getX() - 3
    p2_x = center_point.getX() + 3
    y = center_point.getY() + 3.5
    left_eye = Circle(Point(p1_x, y), 2.5)
    right_eye = Circle(Point(p2_x, y), 2.5)
    return left_eye, right_eye


def move_face(lst, dx, dy):
    for item in lst:
        item.move(dx, dy)



def get_directions(head, dx, dy):
    if head.getCenter().getX() + 10 == 100:
        dx = -1
    if head.getCenter().getX() - 10 == 0:
        dx = 1
    if head.getCenter().getY() + 10 == 100:
        dy = -1
    if head.getCenter().getY() - 10 == 0:
        dy = 1
    return dx, dy


def main():
    win = GraphWin("Bouncing Face", 1600, 1200)
    win.setCoords(0,0,100,100)

    face = []
    head = Circle(Point(50, 50), 10)
    fill_color = "yellow"

    nose = calculate_nose(head.getCenter())
    mouth = calculate_mouth(head.getCenter())
    left_eye, right_eye = calculate_eyes(head.getCenter())
    face.append(head)
    face.append(nose)
    face.append(mouth)
    face.append(left_eye)
    face.append(right_eye)
    head.setFill(fill_color)
    dx = 1
    dy = 1
    for item in face:
        item.draw(win)
    while True:
        head.setFill(fill_color)
        dx, dy = get_directions(head, dx, dy)
        move_face(face, dx, dy)
        button = win.checkKey()
        match button:
            case "q":
                break
            case "w":
                fill_color = "white"
            case "r":
                fill_color = "red"
        update(30)

if __name__ == "__main__":
    main()
