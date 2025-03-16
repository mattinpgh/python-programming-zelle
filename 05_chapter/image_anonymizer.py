from graphics import Point, GraphWin, Circle, Oval, Polygon, Image, Line
from math import sqrt


def draw_eyes(face, window):
    EYE_DISTANCE_RATIO = 0.35
    EYE_SIZE_RATIO = 0.12
    EYE_HEIGHT_RATIO = 0.15

    size = face.getRadius()
    center = face.getCenter()

    eye_distance_from_center = size * EYE_DISTANCE_RATIO
    eye_radius = size * EYE_SIZE_RATIO
    eye_height_from_center = size * EYE_HEIGHT_RATIO

    left_eye_center = Point((center.getX() - eye_distance_from_center), (center.getY() + eye_height_from_center))
    right_eye_center = Point((center.getX() + eye_distance_from_center), (center.getY() + eye_height_from_center))

    left_eye = Circle(left_eye_center, eye_radius)
    right_eye = Circle(right_eye_center, eye_radius)
    left_pupil = Circle(left_eye_center, eye_radius/2)
    right_pupil = Circle(right_eye_center, eye_radius/2)

    left_eye.setOutline("black")
    right_eye.setOutline("black")
    left_pupil.setFill("black")
    right_pupil.setFill("black")

    left_eye.draw(window)
    left_pupil.draw(window)
    right_eye.draw(window)
    right_pupil.draw(window)


def draw_nose(center, size, window):
    NOSE_WIDTH_RATIO = 0.25
    NOSE_TOP_POSITION_RATIO = 0.05
    NOSE_LENGTH_RATIO = 0.25

    nose_width = size * NOSE_WIDTH_RATIO
    nose_top_position = size * NOSE_TOP_POSITION_RATIO
    nose_length = size * NOSE_LENGTH_RATIO

    nose_left = Point((center.getX() - (nose_width / 2)), (center.getY() - nose_top_position))
    nose_right = Point((center.getX() + (nose_width / 2)), (center.getY() - nose_top_position))
    nose_bottom = Point(center.getX(), (center.getY() - nose_top_position + nose_length))

    nose = Polygon(nose_left, nose_right, nose_bottom)
    nose.setOutline("black")
    nose.draw(window)


def draw_mouth(center, size, window):
    MOUTH_WIDTH_RATIO = 0.4
    MOUTH_HEIGHT_RATIO = 0.1
    MOUTH_POSITION_RATIO = 0.3

    mouth_width = size * MOUTH_WIDTH_RATIO
    mouth_height = size * MOUTH_HEIGHT_RATIO
    mouth_position = size * MOUTH_POSITION_RATIO

    mouth_top_left = Point((center.getX() - mouth_width / 2), (center.getY() - mouth_position + (mouth_height / 2)))
    mouth_bottom_right = Point((center.getX() + mouth_width / 2), (center.getY() - mouth_position - (mouth_height / 2)))

    mouth = Oval(mouth_top_left, mouth_bottom_right)
    mouth.setOutline("black")
    mouth.draw(window)


def draw_face(center, size, window):
    face = Circle(center, size)
    face.setOutline("black")
    face.setFill("white")

    face.draw(window)
    draw_eyes(face, window)
    draw_nose(center, size, window)
    draw_mouth(center, size, window)


def main():
    win = GraphWin("F-f-f-face", 1920, 1080)
    win.setCoords(0, 0, 1000, 562)
    testy = Image(Point(500, 231), "test_pic.gif")
    testy.draw(win)
    num_faces = int(input("How many faces will you need to draw? "))

    while num_faces > 0:
        center = win.getMouse()
        border = win.getMouse()

        temp_line = Line(center, border)
        dx = temp_line.getP2().getX() - temp_line.getP1().getX()
        dy = temp_line.getP2().getY() - temp_line.getP1().getY()
        length = sqrt((dx ** 2) + (dy ** 2))

        draw_face(center, length, win)
        num_faces -= 1

    win.getMouse()

main()
