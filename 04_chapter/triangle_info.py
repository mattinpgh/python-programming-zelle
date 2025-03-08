from math import sqrt
from graphics import GraphWin, Text, Polygon, Point


def get_length(point1, point2):
    dx = point1.getX() - point2.getX()
    dy = point1.getY() - point2.getY()
    return sqrt((dx ** 2) + (dy ** 2))


def get_perimeter(point1, point2, point3):
    lst = [
        get_length(point1, point2),
        get_length(point2, point3),
        get_length(point3, point1)
    ]
    return sum(lst)


def get_area(point1, point2, point3):
    a = get_length(point1, point2)
    b = get_length(point2, point3)
    c = get_length(point3, point1)
    s = (a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c))


def main():
    win = GraphWin("Triangle Information", 1280, 800)
    win.setCoords(-10, -10, 10, 10)

    message = "Click in three locations to create a triangle."
    message_display = Text(Point(0, -8), message)
    message_display.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    triangle = Polygon(p1, p2, p3)
    triangle.setOutline("black")
    triangle.draw(win)

    message = (
        f"The vertices of the triangle are: "
        f"({p1.getX():.2f}, {p1.getY():.2f}), "
        f"({p2.getX():.2f}, {p2.getY():.2f}), and "
        f"({p3.getX():.2f}, {p3.getY():.2f})\n"
        f"The perimeter of the triangle is {get_perimeter(p1, p2, p3):.2f}\n"
        f"The area of the triangle is {get_area(p1, p2, p3):.2f}\n\n"
        "Click anywhere to exit."
    )
    message_display.setText(message)
    win.getMouse()


main()
