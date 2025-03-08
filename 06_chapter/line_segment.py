from graphics import *
from math import sqrt


def main():
    win = GraphWin("Line Segment Information", 1280, 800)
    win.setCoords(-10, -10, 10, 10)

    message_display = Text(Point(0, -8), "Click in two locations to create a line segment.")
    message_display.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    new_line = Line(p1, p2)
    midpoint = Circle(new_line.getCenter(), 0.1)
    
    midpoint.setFill("cyan")
    new_line.setFill("black")
    new_line.draw(win)
    midpoint.draw(win)

    dx = new_line.getP2().getX() - new_line.getP1().getX()
    dy = new_line.getP2().getY() - new_line.getP1().getY()

    new_line_slope = dy / dx
    new_line_length = sqrt((dx ** 2) + (dy ** 2))


    message_display.setText(f"p1 is {p1} and p2 is {p2}\nThe slope is {new_line_slope}.\nThe line's length is {new_line_length}\nClick anywhere to exit.")

    win.getMouse()

main()
